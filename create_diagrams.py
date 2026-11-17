#!/usr/bin/env python3
"""Gera os diagramas públicos do portfólio.

Regra editorial: nenhum nome de cliente ou agência, nenhum identificador de
contêiner/propriedade/aplicativo, nenhum schema interno e nenhuma métrica
exata. Apenas arquitetura de referência e capacidade técnica.

Uso: python create_diagrams.py
"""

from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"
ASSETS.mkdir(exist_ok=True)

W = 960
FONT = "Segoe UI, Roboto, Helvetica, Arial, sans-serif"

BLUE = "#1D4ED8"
GREEN = "#15803D"
AMBER = "#B45309"
PURPLE = "#6D28D9"
SLATE = "#475569"
RED = "#B91C1C"


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def header(title: str, badge: str, height: int) -> str:
    badge_w = len(badge) * 7 + 24
    return f"""  <rect width="{W}" height="{height}" rx="16" fill="#F8FAFC"/>
  <rect x="1" y="1" width="{W - 2}" height="{height - 2}" rx="15" fill="none" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="0" y="0" width="{W}" height="52" rx="16" fill="#0F172A"/>
  <rect x="0" y="36" width="{W}" height="16" fill="#0F172A"/>
  <text x="24" y="33" font-family="{FONT}" font-size="16" font-weight="700" fill="#FFFFFF">{esc(title)}</text>
  <rect x="{W - 24 - badge_w}" y="14" width="{badge_w}" height="24" rx="12" fill="#1E293B"/>
  <text x="{W - 24 - badge_w / 2}" y="31" font-family="{FONT}" font-size="11" font-weight="700" fill="#93C5FD" text-anchor="middle">{esc(badge)}</text>"""


def columns(cols: list[dict], ch: int) -> str:
    n = len(cols)
    margin, gap = 30, 18
    cw = (W - 2 * margin - (n - 1) * gap) / n
    y0 = 78
    out = []

    for i, col in enumerate(cols):
        x = margin + i * (cw + gap)
        color = col["color"]
        out.append("  <g>")
        out.append(
            f'    <rect x="{x}" y="{y0}" width="{cw}" height="{ch}" rx="12" '
            f'fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>'
        )
        out.append(
            f'    <rect x="{x}" y="{y0}" width="{cw}" height="38" rx="12" fill="{color}"/>'
        )
        out.append(
            f'    <rect x="{x}" y="{y0 + 26}" width="{cw}" height="12" fill="{color}"/>'
        )
        out.append(
            f'    <text x="{x + cw / 2}" y="{y0 + 24}" font-family="{FONT}" '
            f'font-size="11.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">'
            f'{esc(col["title"])}</text>'
        )

        yy = y0 + 66
        for label, lines in col["items"]:
            out.append(
                f'    <text x="{x + 14}" y="{yy}" font-family="{FONT}" font-size="10.5" '
                f'font-weight="700" fill="#0F172A">{esc(label)}</text>'
            )
            for line in lines:
                yy += 15
                out.append(
                    f'    <text x="{x + 14}" y="{yy}" font-family="{FONT}" font-size="8.8" '
                    f'fill="#475569">{esc(line)}</text>'
                )
            yy += 24
        out.append("  </g>")

        if i < n - 1:
            ax = x + cw + 1
            out.append(
                f'  <path d="M {ax} {y0 + ch / 2} L {ax + gap - 4} {y0 + ch / 2}" '
                f'stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)"/>'
            )

    return "\n".join(out)


def render(title: str, badge: str, cols: list[dict]) -> str:
    max_items = max(len(col["items"]) for col in cols)
    ch = {1: 170, 2: 236, 3: 302}[max_items]
    height = 78 + ch + 22
    defs = """  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#94A3B8"/>
    </marker>
  </defs>"""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" '
        f'width="100%" height="100%" role="img" aria-label="{esc(title)}">\n'
        f"{header(title, badge, height)}\n{defs}\n{columns(cols, ch)}\n</svg>\n"
    )


DIAGRAMS = {
    "architecture_data_layers.svg": render(
        "MODELO DE DADOS EM CAMADAS — DA INGESTÃO AO CONSUMO",
        "ANALYTICS ENGINEERING",
        [
            {
                "title": "FONTES",
                "color": AMBER,
                "items": [
                    ("Mídia paga", ["APIs das plataformas", "Métricas diárias"]),
                    ("Leads", ["Site e formulários", "Mensageria"]),
                    ("Transações", ["Pedidos e receita"]),
                ],
            },
            {
                "title": "NORMALIZAÇÃO",
                "color": SLATE,
                "items": [
                    ("Tipagem e moeda", ["Padronização de campos"]),
                    ("Deduplicação", ["Chaves compostas"]),
                    ("Dimensões", ["Correspondência de IDs"]),
                ],
            },
            {
                "title": "TRANSFORMAÇÃO",
                "color": BLUE,
                "items": [
                    ("Incremental", ["Reprocessamento", "Conversões tardias"]),
                    ("Qualidade", ["Unicidade", "Não-nulidade"]),
                    ("Idempotência", ["Sem duplicidade"]),
                ],
            },
            {
                "title": "CONSUMO",
                "color": GREEN,
                "items": [
                    ("BI executivo", ["Dashboards"]),
                    ("Métricas", ["CPL e CPA"]),
                    ("Decisão", ["Operação e liderança"]),
                ],
            },
        ],
    ),
    "architecture_crossdomain_privacy.svg": render(
        "TRACKING CROSS-DOMAIN — PRIVACIDADE E CONFIRMAÇÃO DE PERSISTÊNCIA",
        "PRIVACY BY DESIGN",
        [
            {
                "title": "USUÁRIO",
                "color": SLATE,
                "items": [
                    ("Formulário B2B", ["Landing page", "Iframe encapsulado"]),
                    ("Privacidade", ["Consentimento", "Dados minimizados"]),
                ],
            },
            {
                "title": "IFRAME",
                "color": BLUE,
                "items": [
                    ("Captura", ["Validação de campos", "Pseudonimização"]),
                    ("Mensageria", ["Evento estruturado"]),
                ],
            },
            {
                "title": "BACKEND",
                "color": AMBER,
                "items": [
                    ("Persistência", ["Envio ao endpoint", "Confirmação de sucesso"]),
                    ("Resiliência", ["Falha não gera conversão"]),
                ],
            },
            {
                "title": "DOMÍNIO PAI",
                "color": GREEN,
                "items": [
                    ("Conversão", ["DataLayer", "GA4 e CAPI"]),
                    ("Mídia", ["Enhanced Conversions"]),
                ],
            },
        ],
    ),
    "architecture_tracking_hybrid.svg": render(
        "COLETA HÍBRIDA — CLIENT-SIDE, SERVER-SIDE E APIS DE CONVERSÃO",
        "ATRIBUIÇÃO",
        [
            {
                "title": "CLIENT-SIDE",
                "color": SLATE,
                "items": [
                    ("Web e app", ["DataLayer", "Eventos de e-commerce"]),
                    ("Consentimento", ["CMP integrada"]),
                ],
            },
            {
                "title": "SERVER-SIDE",
                "color": BLUE,
                "items": [
                    ("Coleta first-party", ["Proxy próprio", "Sessão preservada"]),
                    ("Enriquecimento", ["Contexto do evento"]),
                ],
            },
            {
                "title": "APIS DE CONVERSÃO",
                "color": GREEN,
                "items": [
                    ("Sinais de mídia", ["Meta CAPI", "Pinterest CAPI"]),
                    ("Resiliência", ["Servidor a servidor"]),
                ],
            },
            {
                "title": "ANALYTICS",
                "color": PURPLE,
                "items": [
                    ("BigQuery", ["Export diário", "Reconciliação"]),
                    ("Governança", ["Métricas conciliadas"]),
                ],
            },
        ],
    ),
    "architecture_tag_performance.svg": render(
        "PERFORMANCE DE TAGS — DIAGNÓSTICO, LIMPEZA E CORE WEB VITALS",
        "PERFORMANCE",
        [
            {
                "title": "DIAGNÓSTICO",
                "color": RED,
                "items": [
                    ("Contêiner sobrecarregado", ["Tags legadas", "Scripts duplicados"]),
                    ("Sintomas", ["LCP e INP piores", "TBT elevado"]),
                ],
            },
            {
                "title": "AUDITORIA",
                "color": AMBER,
                "items": [
                    ("Inventário", ["Dependências", "Consentimento"]),
                    ("Priorização", ["Impacto por tag"]),
                ],
            },
            {
                "title": "AÇÕES",
                "color": BLUE,
                "items": [
                    ("Limpeza", ["Remoção em lote", "Lazy load"]),
                    ("Consentimento", ["CMP regularizada"]),
                ],
            },
            {
                "title": "RESULTADO",
                "color": GREEN,
                "items": [
                    ("Core Web Vitals", ["Menos payload", "LCP e INP melhores"]),
                    ("Mídia", ["Quality Score"]),
                ],
            },
        ],
    ),
    "architecture_intraday_observability.svg": render(
        "FUNIL INTRADAY E OBSERVABILIDADE — DO EVENTO AO ALERTA",
        "OPERAÇÃO",
        [
            {
                "title": "EVENTOS",
                "color": SLATE,
                "items": [
                    ("Funil de e-commerce", ["Etapas por hora", "Dispositivo e região"]),
                    ("Telemetria", ["Eventos validados"]),
                ],
            },
            {
                "title": "MODELO GOLD",
                "color": BLUE,
                "items": [
                    ("Agregação horária", ["Canal de mídia", "Visão intradiária"]),
                    ("Qualidade", ["Reconciliação diária"]),
                ],
            },
            {
                "title": "OBSERVABILIDADE",
                "color": AMBER,
                "items": [
                    ("Monitor contínuo", ["Telemetria de tags", "Detecção de anomalias"]),
                    ("Alertas", ["Canal do time"]),
                ],
            },
            {
                "title": "AÇÃO",
                "color": GREEN,
                "items": [
                    ("Alerta e correção", ["Alerta no Slack", "Resposta rápida"]),
                    ("Aprendizado", ["Ajuste de bids"]),
                ],
            },
        ],
    ),
    "architecture_mobile_telemetry.svg": render(
        "TELEMETRIA MOBILE — ESPECIFICAÇÃO, HOMOLOGAÇÃO E PARIDADE",
        "MOBILE",
        [
            {
                "title": "ESPECIFICAÇÃO",
                "color": SLATE,
                "items": [
                    ("Plano de tagueamento", ["Jornadas e eventos", "Dicionário de dados"]),
                    ("Governança", ["Revisão com o time"]),
                ],
            },
            {
                "title": "MIGRAÇÃO",
                "color": BLUE,
                "items": [
                    ("Nativo para Flutter", ["Paridade de eventos", "Receita e planos"]),
                    ("Risco", ["Eventos duplicados"]),
                ],
            },
            {
                "title": "HOMOLOGAÇÃO",
                "color": AMBER,
                "items": [
                    ("ADB e Logcat", ["Modo verbose", "Payloads de rede"]),
                    ("Critério", ["Paridade com legado"]),
                ],
            },
            {
                "title": "ATRIBUIÇÃO",
                "color": GREEN,
                "items": [
                    ("Modelagem", ["Conversões diárias", "Loja e analytics"]),
                    ("Leitura", ["Aquisição e receita"]),
                ],
            },
        ],
    ),
}


def main() -> None:
    for filename, content in DIAGRAMS.items():
        path = ASSETS / filename
        path.write_text(content, encoding="utf-8")
        print(f"ok: {path.name}")
    print("Diagramas acadêmicos (BuscaRM e KDD) são mantidos como arquivos estáticos.")


if __name__ == "__main__":
    main()
