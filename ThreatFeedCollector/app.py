import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from pymongo import MongoClient
import config  # Your config.py with MONGO_URI, DB_NAME, COLLECTION_NAME

# Connect to MongoDB Atlas using config.py
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
ioc_collection = db[config.COLLECTION_NAME]

def get_ioc_stats():
    """
    Aggregate IOC counts by 'type' field.
    Handles None types by labeling as 'UNKNOWN'.
    """
    pipeline = [
        {"$group": {"_id": "$type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    stats = list(ioc_collection.aggregate(pipeline))
    return {
        (str(stat["_id"]).upper() if stat["_id"] is not None else "UNKNOWN"): stat["count"]
        for stat in stats
    }

def get_threat_reports(query=""):
    """
    Fetch IOC documents matching the query in 'value' field.
    Case-insensitive regex search, limited to 50 results.
    """
    results = list(ioc_collection.find({"value": {"$regex": query, "$options": "i"}}).limit(50))
    return results

# External stylesheets: Bootstrap dark theme + custom CSS
external_stylesheets = [
    dbc.themes.CYBORG,  # Dark theme
    "/assets/custom.css"  # Your custom CSS file path
]

app = dash.Dash(_name_, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
app.title = "Threat Intelligence Dashboard"

app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="ThreatIntel Dashboard",
        color="dark",
        dark=True,
        className="mb-4 navbar"
    ),

    dbc.Row([
        dbc.Col([
            html.H3("IOC Summary", className="mb-3"),
            dbc.Row([
                dbc.Col(html.Div(id="ip-metric", className="metric card p-3"), width=2),
                dbc.Col(html.Div(id="domain-metric", className="metric card p-3"), width=2),
                dbc.Col(html.Div(id="url-metric", className="metric card p-3"), width=2),
                dbc.Col(html.Div(id="md5-metric", className="metric card p-3"), width=2),
                dbc.Col(html.Div(id="sha256-metric", className="metric card p-3"), width=2),
                dbc.Col(html.Div(id="cve-metric", className="metric card p-3"), width=2),
            ])
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Input(
                id="search-box",
                placeholder="🔍 Search threats, IOCs, CVEs...",
                type="text",
                debounce=True,
                className="form-control mb-4"
            ),
            html.Div(id="threat-list")
        ], width=12)
    ])
], fluid=True)

@app.callback(
    [Output("ip-metric", "children"),
     Output("domain-metric", "children"),
     Output("url-metric", "children"),
     Output("md5-metric", "children"),
     Output("sha256-metric", "children"),
     Output("cve-metric", "children")],
    [Input("search-box", "value")]
)
def update_metrics(query):
    stats = get_ioc_stats()
    return (
        f"🌐 IPs: {stats.get('IP', 0)}",
        f"🔗 Domains: {stats.get('DOMAIN', 0)}",
        f"🌍 URLs: {stats.get('URL', 0)}",
        f"🔒 MD5: {stats.get('MD5', 0)}",
        f"🧬 SHA256: {stats.get('SHA256', 0)}",
        f"🛡 CVEs: {stats.get('CVE', 0)}"
    )

@app.callback(
    Output("threat-list", "children"),
    [Input("search-box", "value")]
)
def update_threat_list(query):
    reports = get_threat_reports(query or "")
    if not reports:
        return dbc.Alert("No threats found.", color="secondary")
    cards = []
    for r in reports:
        ioc_badges = [html.Span(val, className="ioc-badge") for val in [r.get("value", "N/A")]]
        cards.append(
            dbc.Card([
                dbc.CardHeader([
                    html.Strong(r.get("type", "IOC")),
                    html.Span(f" | Source: {r.get('source', 'Unknown')}", className="ms-2 text-info"),
                ]),
                dbc.CardBody([
                    html.Div(ioc_badges),
                    html.Div(f"Timestamp: {r.get('timestamp', 'N/A')}", className="text-secondary"),
                ])
            ], className="mb-3 card shadow-lg")
        )
    return cards

if _name_ == "_main_":
    app.run(debug=True)