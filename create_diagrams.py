import os

assets_dir = r"c:\Users\marco\OneDrive\Documentos\analytics\portfolio\assets"
os.makedirs(assets_dir, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Grupo Zelo — Arquitetura Medalhão & Dataform ELT (KDD & CRISP-DM)
# -----------------------------------------------------------------------------
svg_zelo = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1A73E8"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E8E3E"/>
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#7B1FA2"/>
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect width="960" height="420" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="418" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#1A73E8"/>
  <rect x="0" y="32" width="960" height="16" fill="#1A73E8"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">GRUPO ZELO — ARQUITETURA MEDALHÃO & DATAFORM ELT INCREMENTAL</text>
  <rect x="760" y="12" width="176" height="24" rx="12" fill="#E8F0FE"/>
  <text x="848" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#1967D2" text-anchor="middle">KDD + CRISP-DM</text>

  <!-- COLUMN 1: BRONZE (RAW / DATA UNDERSTANDING) -->
  <g transform="translate(30, 70)" filter="url(#m3-shadow)">
    <rect width="180" height="320" rx="12" fill="#FFFFFF" stroke="#DADCE0" stroke-width="1.5"/>
    <rect width="180" height="36" rx="12" fill="#F1F3F4"/>
    <rect y="24" width="180" height="12" fill="#F1F3F4"/>
    <text x="90" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#3C4043" text-anchor="middle">1. CAMADA BRONZE (RAW)</text>
    <text x="90" y="52" font-family="Roboto, sans-serif" font-size="10" font-weight="500" fill="#5F6368" text-anchor="middle">KDD: Data Selection</text>

    <!-- Cards Inside Bronze -->
    <rect x="12" y="65" width="156" height="60" rx="8" fill="#F8F9FA" stroke="#E8EAED"/>
    <text x="22" y="86" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#202124">Google Ads API</text>
    <text x="22" y="103" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Campanhas e Métricas Diárias</text>
    <text x="22" y="116" font-family="Roboto, sans-serif" font-size="9" fill="#70757A">Segmentação de Contas</text>

    <rect x="12" y="140" width="156" height="60" rx="8" fill="#F8F9FA" stroke="#E8EAED"/>
    <text x="22" y="161" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#202124">Meta Graph API</text>
    <text x="22" y="178" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Instant Forms & Lead Gen</text>
    <text x="22" y="191" font-family="Roboto, sans-serif" font-size="9" fill="#70757A">Pixel / CAPI Events</text>

    <rect x="12" y="215" width="156" height="60" rx="8" fill="#F8F9FA" stroke="#E8EAED"/>
    <text x="22" y="236" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#202124">GA4 Streaming Export</text>
    <text x="22" y="253" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Leads Web e WhatsApp</text>
    <text x="22" y="266" font-family="Roboto, sans-serif" font-size="9" fill="#70757A">generate_lead, click_wpp</text>

    <rect x="12" y="285" width="156" height="24" rx="6" fill="#F1F3F4"/>
    <text x="90" y="301" font-family="Roboto, sans-serif" font-size="9" font-weight="600" fill="#5F6368" text-anchor="middle">Ingestão Automática diária</text>
  </g>

  <!-- Connectors Bronze -> Silver -->
  <path d="M 210 230 L 260 230" stroke="#1A73E8" stroke-width="2" fill="none" marker-end="url(#arrow-blue)"/>

  <!-- COLUMN 2: SILVER (DATA PREPARATION & QUALITY) -->
  <g transform="translate(260, 70)" filter="url(#m3-shadow)">
    <rect width="190" height="320" rx="12" fill="#FFFFFF" stroke="#DADCE0" stroke-width="1.5"/>
    <rect width="190" height="36" rx="12" fill="#E8F0FE"/>
    <rect y="24" width="190" height="12" fill="#E8F0FE"/>
    <text x="95" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#1967D2" text-anchor="middle">2. CAMADA SILVER</text>
    <text x="95" y="52" font-family="Roboto, sans-serif" font-size="10" font-weight="500" fill="#1A73E8" text-anchor="middle">KDD: Pre-processing & Cleaning</text>

    <!-- Cards Inside Silver -->
    <rect x="12" y="65" width="166" height="52" rx="8" fill="#F8F9FA" stroke="#D2E3FC"/>
    <text x="22" y="85" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1967D2">slv_gads_performance</text>
    <text x="22" y="102" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Tipagem, BRL casting, normalização</text>

    <rect x="12" y="125" width="166" height="52" rx="8" fill="#F8F9FA" stroke="#D2E3FC"/>
    <text x="22" y="145" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1967D2">slv_meta_performance</text>
    <text x="22" y="162" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Equalização de métricas on-site/off</text>

    <rect x="12" y="185" width="166" height="52" rx="8" fill="#F8F9FA" stroke="#D2E3FC"/>
    <text x="22" y="205" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1967D2">slv_ga4_leads_zelo</text>
    <text x="22" y="222" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Filtro de hostnames e deduplicação</text>

    <rect x="12" y="245" width="166" height="60" rx="8" fill="#E8F0FE" stroke="#AECBFA"/>
    <text x="22" y="265" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#174EA6">slv_dim_campaigns</text>
    <text x="22" y="280" font-family="Roboto, sans-serif" font-size="8.5" fill="#1967D2">Mapeamento De-Para Cemitérios</text>
    <text x="22" y="294" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Fallback Join: Nome &gt; ID</text>
  </g>

  <!-- Connectors Silver -> Dataform Engine -->
  <path d="M 450 230 L 500 230" stroke="#7B1FA2" stroke-width="2" fill="none" marker-end="url(#arrow-purple)"/>

  <!-- COLUMN 3: DATAFORM ENGINE (INCREMENTAL PIPELINE & ASSERTIONS) -->
  <g transform="translate(500, 70)" filter="url(#m3-shadow)">
    <rect width="210" height="320" rx="12" fill="#FFFFFF" stroke="#E1BEE7" stroke-width="1.5"/>
    <rect width="210" height="36" rx="12" fill="#F3E5F5"/>
    <rect y="24" width="210" height="12" fill="#F3E5F5"/>
    <text x="105" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#7B1FA2" text-anchor="middle">3. MOTOR DATAFORM (SQLX)</text>
    <text x="105" y="52" font-family="Roboto, sans-serif" font-size="10" font-weight="500" fill="#8E24AA" text-anchor="middle">Transformation & Idempotência</text>

    <!-- Card Lookback -->
    <rect x="12" y="65" width="186" height="70" rx="8" fill="#FAF5FB" stroke="#CE93D8"/>
    <text x="22" y="85" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#6A1B9A">Incremental Lookback (7d)</text>
    <text x="22" y="101" font-family="Consolas, monospace" font-size="8.5" fill="#4A148C">when(incremental(), ...)</text>
    <text x="22" y="115" font-family="Roboto, sans-serif" font-size="8.5" fill="#616161">Absorve conversões tardias</text>
    <text x="22" y="127" font-family="Roboto, sans-serif" font-size="8.5" fill="#616161">Limita scan no BigQuery</text>

    <!-- Card Idempotência -->
    <rect x="12" y="145" width="186" height="70" rx="8" fill="#FAF5FB" stroke="#CE93D8"/>
    <text x="22" y="165" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#6A1B9A">Pre-operations: DELETE</text>
    <text x="22" y="181" font-family="Consolas, monospace" font-size="8" fill="#4A148C">DELETE FROM ${self()} WHERE</text>
    <text x="22" y="194" font-family="Consolas, monospace" font-size="8" fill="#4A148C">date &gt;= DATE_SUB(..., 7 DAY)</text>
    <text x="22" y="207" font-family="Roboto, sans-serif" font-size="8.5" font-weight="600" fill="#2E7D32">Garantia total de Idempotência</text>

    <!-- Card Assertions -->
    <rect x="12" y="225" width="186" height="80" rx="8" fill="#F3E5F5" stroke="#BA68C8"/>
    <text x="22" y="245" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#4A148C">Data Quality Assertions</text>
    <text x="22" y="261" font-family="Roboto, sans-serif" font-size="8.5" fill="#6A1B9A">• uniqueKey: [date, source, camp_id]</text>
    <text x="22" y="275" font-family="Roboto, sans-serif" font-size="8.5" fill="#6A1B9A">• nonNull: [date, source, camp_id]</text>
    <text x="22" y="292" font-family="Roboto, sans-serif" font-size="8.5" font-weight="700" fill="#C2185B">Zero duplicidade em produção</text>
  </g>

  <!-- Connectors Dataform -> Gold -->
  <path d="M 710 230 L 760 230" stroke="#1E8E3E" stroke-width="2" fill="none" marker-end="url(#arrow-green)"/>

  <!-- COLUMN 4: GOLD (BUSINESS INTELLIGENCE & EVALUATION) -->
  <g transform="translate(760, 70)" filter="url(#m3-shadow)">
    <rect width="170" height="320" rx="12" fill="#FFFFFF" stroke="#C8E6C9" stroke-width="1.5"/>
    <rect width="170" height="36" rx="12" fill="#E6F4EA"/>
    <rect y="24" width="170" height="12" fill="#E6F4EA"/>
    <text x="85" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#137333" text-anchor="middle">4. CAMADA GOLD & BI</text>
    <text x="85" y="52" font-family="Roboto, sans-serif" font-size="10" font-weight="500" fill="#1E8E3E" text-anchor="middle">KDD: Interpretation & Value</text>

    <!-- Card Gold Tables -->
    <rect x="10" y="65" width="150" height="75" rx="8" fill="#F8F9FA" stroke="#CEEAD6"/>
    <text x="18" y="85" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#137333">gld_marketing_perf</text>
    <text x="18" y="100" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Mídia Google + Meta</text>
    <text x="18" y="114" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Particionada por Date</text>
    <text x="18" y="128" font-family="Roboto, sans-serif" font-size="8.5" fill="#1E8E3E">Cluster: source, campaign</text>

    <rect x="10" y="150" width="150" height="65" rx="8" fill="#F8F9FA" stroke="#CEEAD6"/>
    <text x="18" y="170" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#137333">gld_leads_zelo</text>
    <text x="18" y="186" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Leads Cross-channel</text>
    <text x="18" y="200" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">CPA / CPL por Cemitério</text>

    <!-- Card Dashboards -->
    <rect x="10" y="225" width="150" height="80" rx="8" fill="#E6F4EA" stroke="#A8DAB5"/>
    <text x="18" y="245" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#0D652D">Consumo Executivo</text>
    <text x="18" y="262" font-family="Roboto, sans-serif" font-size="9" font-weight="600" fill="#137333">• Dashboards Metabase</text>
    <text x="18" y="278" font-family="Roboto, sans-serif" font-size="9" font-weight="600" fill="#137333">• Relatórios Looker Studio</text>
    <text x="18" y="294" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Decisão Estratégica em Tempo Real</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_medallion_zelo.svg"), "w", encoding="utf-8") as f:
    f.write(svg_zelo)

# -----------------------------------------------------------------------------
# 2. FastShop Empresas — Cross-Domain Tracking Seguro via Iframe & SubtleCrypto SHA-256
# -----------------------------------------------------------------------------
svg_fastshop = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-fast" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1A73E8"/>
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E8E3E"/>
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#F9AB00"/>
    </marker>
  </defs>

  <rect width="960" height="400" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="398" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#0D47A1"/>
  <rect x="0" y="32" width="960" height="16" fill="#0D47A1"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">FASTSHOP EMPRESAS — TRACKING CROSS-DOMAIN SEGURO (IFRAME + SHA-256 CLIENT)</text>
  <rect x="790" y="12" width="146" height="24" rx="12" fill="#E3F2FD"/>
  <text x="863" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#0D47A1" text-anchor="middle">PRIVACY BY DESIGN</text>

  <!-- Lifeline Columns (Sequence Diagram) -->
  <g transform="translate(40, 65)">
    <!-- Actor 1: Usuário -->
    <rect x="20" y="10" width="140" height="36" rx="8" fill="#FFFFFF" stroke="#DADCE0" stroke-width="1.5" filter="url(#m3-shadow-fast)"/>
    <text x="90" y="33" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#202124" text-anchor="middle">Usuário B2B</text>
    <line x1="90" y1="46" x2="90" y2="300" stroke="#BDC1C6" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Actor 2: Iframe Form -->
    <rect x="240" y="10" width="170" height="36" rx="8" fill="#E8F0FE" stroke="#AECBFA" stroke-width="1.5" filter="url(#m3-shadow-fast)"/>
    <text x="325" y="27" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1967D2" text-anchor="middle">Iframe Formulario</text>
    <text x="325" y="39" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368" text-anchor="middle">/cloud &amp; /locacao</text>
    <line x1="325" y1="46" x2="325" y2="300" stroke="#BDC1C6" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Actor 3: Middleware API -->
    <rect x="490" y="10" width="160" height="36" rx="8" fill="#FEF7E0" stroke="#FEEFC3" stroke-width="1.5" filter="url(#m3-shadow-fast)"/>
    <text x="570" y="27" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#B06000" text-anchor="middle">Middleware Lead API</text>
    <text x="570" y="39" font-family="Roboto, sans-serif" font-size="8.5" fill="#70757A" text-anchor="middle">POST /lead endpoint</text>
    <line x1="570" y1="46" x2="570" y2="300" stroke="#BDC1C6" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Actor 4: Parent Domain & GTM -->
    <rect x="710" y="10" width="170" height="36" rx="8" fill="#E6F4EA" stroke="#A8DAB5" stroke-width="1.5" filter="url(#m3-shadow-fast)"/>
    <text x="795" y="27" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#137333" text-anchor="middle">Domínio Pai &amp; GTM</text>
    <text x="795" y="39" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368" text-anchor="middle">empresas.fastshop.com.br</text>
    <line x1="795" y1="46" x2="795" y2="300" stroke="#BDC1C6" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- STEP 1: Form Submit -->
    <line x1="90" y1="80" x2="320" y2="80" stroke="#1A73E8" stroke-width="2" marker-end="url(#arr-blue)"/>
    <rect x="135" y="65" width="140" height="20" rx="4" fill="#FFFFFF" stroke="#DADCE0"/>
    <text x="205" y="79" font-family="Roboto, sans-serif" font-size="9" font-weight="600" fill="#3C4043" text-anchor="middle">1. Preenche e Envia Form</text>

    <!-- STEP 2: POST /lead -->
    <line x1="325" y1="120" x2="565" y2="120" stroke="#F9AB00" stroke-width="2" marker-end="url(#arr-amber)"/>
    <rect x="375" y="105" width="140" height="20" rx="4" fill="#FFFFFF" stroke="#F9AB00"/>
    <text x="445" y="119" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#B06000" text-anchor="middle">2. POST /lead Payload</text>

    <!-- STEP 3: HTTP 200 OK Response -->
    <line x1="570" y1="160" x2="330" y2="160" stroke="#1E8E3E" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arr-green)"/>
    <rect x="380" y="145" width="145" height="20" rx="4" fill="#E6F4EA" stroke="#34A853"/>
    <text x="452" y="159" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#137333" text-anchor="middle">3. HTTP 200 OK (Persistido)</text>

    <!-- SUB-STEP: SubtleCrypto SHA-256 Box -->
    <rect x="240" y="185" width="170" height="38" rx="6" fill="#FEF7E0" stroke="#F9AB00" stroke-width="1.5"/>
    <text x="325" y="200" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#B06000" text-anchor="middle">SubtleCrypto (SHA-256)</text>
    <text x="325" y="214" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Hash de Email, Nome e Telefone</text>

    <!-- STEP 4: window.postMessage -->
    <line x1="325" y1="245" x2="790" y2="245" stroke="#1A73E8" stroke-width="2.5" marker-end="url(#arr-blue)"/>
    <rect x="420" y="232" width="280" height="24" rx="6" fill="#E8F0FE" stroke="#1A73E8"/>
    <text x="560" y="248" font-family="Consolas, monospace" font-size="9" font-weight="700" fill="#1967D2" text-anchor="middle">4. postMessage({ event: generate_lead, hashed_pii })</text>

    <!-- STEP 5: dataLayer.push & Conversion -->
    <rect x="710" y="260" width="170" height="42" rx="6" fill="#1E8E3E"/>
    <text x="795" y="278" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">dataLayer.push ➔ GA4 &amp; CAPI</text>
    <text x="795" y="293" font-family="Roboto, sans-serif" font-size="8" fill="#E6F4EA" text-anchor="middle">Enhanced Conversions / Match Rate</text>
  </g>

  <!-- Bottom Metric Box -->
  <rect x="40" y="360" width="880" height="26" rx="6" fill="#E8EAED"/>
  <text x="480" y="377" font-family="Roboto, sans-serif" font-size="10" font-weight="600" fill="#3C4043" text-anchor="middle">✓ 100% de eliminação de leads fantasmas por falhas de rede   |   ✓ Conformidade integral LGPD com anonimização na borda</text>
</svg>'''

with open(os.path.join(assets_dir, "architecture_postmessage_fastshop.svg"), "w", encoding="utf-8") as f:
    f.write(svg_fastshop)

# -----------------------------------------------------------------------------
# 3. Natura & AVON — Arquitetura Híbrida Server-Side & Resolução de Atribuição (KDD)
# -----------------------------------------------------------------------------
svg_natura = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-natura" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
    <marker id="arr-blue2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1A73E8"/>
    </marker>
    <marker id="arr-green2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E8E3E"/>
    </marker>
  </defs>

  <rect width="960" height="400" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="398" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#E65100"/>
  <rect x="0" y="32" width="960" height="16" fill="#E65100"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">NATURA &amp; AVON LATAM — ARQUITETURA DE TRACKING HÍBRIDO SERVER-SIDE &amp; CAPI</text>
  <rect x="780" y="12" width="156" height="24" rx="12" fill="#FFE0B2"/>
  <text x="858" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#E65100" text-anchor="middle">RECONCILIAÇÃO GA4 x BQ</text>

  <!-- TOPOLOGICAL BLOCKS -->
  <!-- 1. Client Layer -->
  <g transform="translate(30, 80)" filter="url(#m3-shadow-natura)">
    <rect width="180" height="280" rx="12" fill="#FFFFFF" stroke="#DADCE0" stroke-width="1.5"/>
    <rect width="180" height="36" rx="12" fill="#FFF3E0"/>
    <rect y="24" width="180" height="12" fill="#FFF3E0"/>
    <text x="90" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#E65100" text-anchor="middle">CLIENT-SIDE (WEB &amp; APP)</text>

    <rect x="12" y="55" width="156" height="65" rx="8" fill="#F8F9FA" stroke="#FFE0B2"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#202124">E-commerces LATAM</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Natura Brasil &amp; América Latina</text>
    <text x="22" y="104" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">AVON Cosméticos</text>

    <rect x="12" y="130" width="156" height="75" rx="8" fill="#FFF8E1" stroke="#FFE082"/>
    <text x="22" y="150" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#B78103">DataLayer E-commerce</text>
    <text x="22" y="166" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• view_item, add_to_cart</text>
    <text x="22" y="180" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• begin_checkout, purchase</text>
    <text x="22" y="194" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Rastreabilidade de UTMs</text>

    <rect x="12" y="215" width="156" height="50" rx="8" fill="#F1F3F4"/>
    <text x="22" y="235" font-family="Roboto, sans-serif" font-size="9.5" font-weight="600" fill="#3C4043">GTM Web Client</text>
    <text x="22" y="250" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Custom JS &amp; Consent Tags</text>
  </g>

  <!-- Connector Client -> Server -->
  <path d="M 210 220 L 260 220" stroke="#E65100" stroke-width="2" fill="none" marker-end="url(#arr-blue2)"/>

  <!-- 2. GTM Server-Side Container (GCP Cloud Run) -->
  <g transform="translate(260, 80)" filter="url(#m3-shadow-natura)">
    <rect width="230" height="280" rx="12" fill="#FFFFFF" stroke="#CE93D8" stroke-width="1.5"/>
    <rect width="230" height="36" rx="12" fill="#F3E5F5"/>
    <rect y="24" width="230" height="12" fill="#F3E5F5"/>
    <text x="115" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#7B1FA2" text-anchor="middle">GTM SERVER-SIDE (GCP)</text>

    <rect x="12" y="55" width="206" height="65" rx="8" fill="#F8F9FA" stroke="#E1BEE7"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#4A148C">Cloud Run Cluster</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Coleta em subdomínio First-party</text>
    <text x="22" y="104" font-family="Roboto, sans-serif" font-size="8.5" fill="#137333">Recuperação de Cookies contra ITP</text>

    <rect x="12" y="130" width="206" height="75" rx="8" fill="#FAF5FB" stroke="#CE93D8"/>
    <text x="22" y="150" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#6A1B9A">Saneamento de Atribuição</text>
    <text x="22" y="166" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Eliminação de quebra cross-domain</text>
    <text x="22" y="180" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Retenção de parâmetros em gateways</text>
    <text x="22" y="194" font-family="Roboto, sans-serif" font-size="8.5" fill="#137333">90%+ de perdas eliminadas</text>

    <rect x="12" y="215" width="206" height="50" rx="8" fill="#F3E5F5"/>
    <text x="22" y="235" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#4A148C">Enriquecimento de Eventos</text>
    <text x="22" y="250" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Hashing seguro e distribuição para APIs</text>
  </g>

  <!-- Connectors Server -> Destinations -->
  <path d="M 490 170 L 540 140" stroke="#1E8E3E" stroke-width="2" fill="none" marker-end="url(#arr-green2)"/>
  <path d="M 490 270 L 540 270" stroke="#1A73E8" stroke-width="2" fill="none" marker-end="url(#arr-blue2)"/>

  <!-- 3. Conversion APIs Destination -->
  <g transform="translate(540, 80)" filter="url(#m3-shadow-natura)">
    <rect width="190" height="130" rx="12" fill="#FFFFFF" stroke="#A8DAB5" stroke-width="1.5"/>
    <rect width="190" height="32" rx="12" fill="#E6F4EA"/>
    <rect y="20" width="190" height="12" fill="#E6F4EA"/>
    <text x="95" y="21" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#137333" text-anchor="middle">APIs DE CONVERSÃO (CAPI)</text>

    <text x="18" y="55" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#0D652D">• Meta Conversions API</text>
    <text x="18" y="70" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Eventos Purchase imunes a AdBlock</text>
    <text x="18" y="90" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#0D652D">• Pinterest Conversions API</text>
    <text x="18" y="105" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Sinal de conversão direto servidor-servidor</text>
  </g>

  <!-- 4. GA4 & BigQuery Layer -->
  <g transform="translate(540, 230)" filter="url(#m3-shadow-natura)">
    <rect width="190" height="130" rx="12" fill="#FFFFFF" stroke="#AECBFA" stroke-width="1.5"/>
    <rect width="190" height="32" rx="12" fill="#E8F0FE"/>
    <rect y="20" width="190" height="12" fill="#E8F0FE"/>
    <text x="95" y="21" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1967D2" text-anchor="middle">GA4 ➔ BIGQUERY EXPORT</text>

    <text x="18" y="55" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#174EA6">Google Analytics 4 Export</text>
    <text x="18" y="70" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Tabelas diárias em BigQuery</text>
    <text x="18" y="90" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#174EA6">Reconciliação Volumétrica</text>
    <text x="18" y="105" font-family="Roboto, sans-serif" font-size="8.5" font-weight="600" fill="#137333">&gt;98% de paridade com ERP transacional</text>
  </g>

  <!-- Connector to Data Science Team -->
  <path d="M 730 295 L 770 295" stroke="#1A73E8" stroke-width="2" fill="none" marker-end="url(#arr-blue2)"/>

  <!-- 5. Data Science / Analytics Models -->
  <g transform="translate(770, 80)" filter="url(#m3-shadow-natura)">
    <rect width="160" height="280" rx="12" fill="#FFFFFF" stroke="#BDC1C6" stroke-width="1.5"/>
    <rect width="160" height="36" rx="12" fill="#F1F3F4"/>
    <rect y="24" width="160" height="12" fill="#F1F3F4"/>
    <text x="80" y="23" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#3C4043" text-anchor="middle">DATA SCIENCE &amp; BI</text>

    <rect x="10" y="55" width="140" height="90" rx="8" fill="#F8F9FA" stroke="#E8EAED"/>
    <text x="18" y="75" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#202124">Modelagem de LTV</text>
    <text x="18" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Alimentação de modelos</text>
    <text x="18" y="103" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">preditivos com dados</text>
    <text x="18" y="116" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">consistentes de receita.</text>

    <rect x="10" y="155" width="140" height="90" rx="8" fill="#F8F9FA" stroke="#E8EAED"/>
    <text x="18" y="175" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#202124">Otimização de CPA</text>
    <text x="18" y="190" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Algoritmos de Smart</text>
    <text x="18" y="203" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Bidding com sinais</text>
    <text x="18" y="216" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">íntegros de conversão.</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_serverside_natura_avon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_natura)

# -----------------------------------------------------------------------------
# 4. Dock — Auditoria de Contêiner & Otimização de Core Web Vitals
# -----------------------------------------------------------------------------
svg_dock = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 380" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-dock" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect width="960" height="380" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="378" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#00796B"/>
  <rect x="0" y="32" width="960" height="16" fill="#00796B"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">FINTECH DOCK — AUDITORIA DE CONTÊINER GTM &amp; CORE WEB VITALS (LCP, INP, TBT)</text>
  <rect x="790" y="12" width="146" height="24" rx="12" fill="#E0F2F1"/>
  <text x="863" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#00796B" text-anchor="middle">WEB PERFORMANCE</text>

  <!-- 3 Comparison Columns -->
  <!-- Col 1: Cenário Anterior (Sobrecarga) -->
  <g transform="translate(30, 75)" filter="url(#m3-shadow-dock)">
    <rect width="280" height="280" rx="12" fill="#FFFFFF" stroke="#FFCDD2" stroke-width="1.5"/>
    <rect width="280" height="36" rx="12" fill="#FFEBEE"/>
    <rect y="24" width="280" height="12" fill="#FFEBEE"/>
    <text x="140" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#C62828" text-anchor="middle">CENÁRIO ANTERIOR (SOBRECARGA)</text>

    <rect x="12" y="55" width="256" height="55" rx="8" fill="#FFF5F5" stroke="#FFCDD2"/>
    <text x="22" y="74" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#B71C1C">81 Tags Legadas de UA</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Pasta 500 inflando o arquivo gtm.js transferido</text>
    <text x="22" y="102" font-family="Roboto, sans-serif" font-size="8.5" fill="#D32F2F">Overhead de parsing e compilação</text>

    <rect x="12" y="120" width="256" height="55" rx="8" fill="#FFF5F5" stroke="#FFCDD2"/>
    <text x="22" y="139" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#B71C1C">Google Optimize Descontinuado</text>
    <text x="22" y="155" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Tag ID 265 gerando flicker e bloqueando render</text>
    <text x="22" y="167" font-family="Roboto, sans-serif" font-size="8.5" fill="#D32F2F">Degradação severa de LCP</text>

    <rect x="12" y="185" width="256" height="75" rx="8" fill="#FFF5F5" stroke="#FFCDD2"/>
    <text x="22" y="204" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#B71C1C">Duplicidade Clarity &amp; Hotjar</text>
    <text x="22" y="220" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Dois scripts de gravação rodando no Page View</text>
    <text x="22" y="233" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">CMP AdOpt pausada gerando risco LGPD</text>
    <text x="22" y="246" font-family="Roboto, sans-serif" font-size="8.5" fill="#D32F2F">Travamentos de Thread / Alto TBT e INP</text>
  </g>

  <!-- Col 2: Plano de Ação & Engenharia -->
  <g transform="translate(340, 75)" filter="url(#m3-shadow-dock)">
    <rect width="280" height="280" rx="12" fill="#FFFFFF" stroke="#B2DFDB" stroke-width="1.5"/>
    <rect width="280" height="36" rx="12" fill="#E0F2F1"/>
    <rect y="24" width="280" height="12" fill="#E0F2F1"/>
    <text x="140" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#00695C" text-anchor="middle">AÇÕES DE ENGENHARIA DE TAGS</text>

    <rect x="12" y="55" width="256" height="55" rx="8" fill="#F0FDF4" stroke="#A7F3D0"/>
    <text x="22" y="74" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#047857">Expurgo em Lote de UA</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Remoção de 81 tags, triggers e variáveis órfãs</text>
    <text x="22" y="102" font-family="Roboto, sans-serif" font-size="8.5" fill="#059669">Redução massiva do payload do container</text>

    <rect x="12" y="120" width="256" height="55" rx="8" fill="#F0FDF4" stroke="#A7F3D0"/>
    <text x="22" y="139" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#047857">Exclusão do Optimize</text>
    <text x="22" y="155" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Eliminação do script síncrono obsoleto</text>
    <text x="22" y="167" font-family="Roboto, sans-serif" font-size="8.5" fill="#059669">Renderização fluida sem travamento</text>

    <rect x="12" y="185" width="256" height="75" rx="8" fill="#F0FDF4" stroke="#A7F3D0"/>
    <text x="22" y="204" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#047857">Lazy Load &amp; Desduplicação</text>
    <text x="22" y="220" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Migração de triggers para Window Loaded</text>
    <text x="22" y="233" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Desduplicação: apenas um gravador ativo</text>
    <text x="22" y="246" font-family="Roboto, sans-serif" font-size="8.5" fill="#059669">• Reativação e auditoria da CMP AdOpt (LGPD)</text>
  </g>

  <!-- Col 3: Ganhos Mensuráveis -->
  <g transform="translate(650, 75)" filter="url(#m3-shadow-dock)">
    <rect width="280" height="280" rx="12" fill="#FFFFFF" stroke="#C8E6C9" stroke-width="1.5"/>
    <rect width="280" height="36" rx="12" fill="#E8F5E9"/>
    <rect y="24" width="280" height="12" fill="#E8F5E9"/>
    <text x="140" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#2E7D32" text-anchor="middle">IMPACTO &amp; GANHOS CORE WEB VITALS</text>

    <rect x="12" y="55" width="256" height="60" rx="8" fill="#F1F8E9" stroke="#C5E1A5"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#33691E">LCP (Largest Contentful Paint)</text>
    <text x="22" y="92" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Aceleração de renderização visual crítica</text>
    <text x="22" y="105" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#2E7D32">Melhora no Índice de Qualidade Google Ads</text>

    <rect x="12" y="125" width="256" height="60" rx="8" fill="#F1F8E9" stroke="#C5E1A5"/>
    <text x="22" y="145" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#33691E">INP (Interaction to Next Paint)</text>
    <text x="22" y="162" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Desobstrução da main thread do browser</text>
    <text x="22" y="175" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#2E7D32">Respostas imediatas a cliques do usuário</text>

    <rect x="12" y="195" width="256" height="65" rx="8" fill="#E8F5E9" stroke="#A5D6A7"/>
    <text x="22" y="215" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1B5E20">Segurança Jurídica &amp; LGPD</text>
    <text x="22" y="232" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Conformidade total no consentimento</text>
    <text x="22" y="246" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#2E7D32">Zero risco regulatório de tracking indevido</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_cwv_dock.svg"), "w", encoding="utf-8") as f:
    f.write(svg_dock)

# -----------------------------------------------------------------------------
# 5. Águia Branca & Observabilidade / Agentic Analytics
# -----------------------------------------------------------------------------
svg_intraday = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-intraday" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect width="960" height="400" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="398" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#311B92"/>
  <rect x="0" y="32" width="960" height="16" fill="#311B92"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">VIAÇÃO ÁGUIA BRANCA &amp; AGENTIC ANALYTICS — FUNIL INTRADAY E OBSERVABILIDADE</text>
  <rect x="760" y="12" width="176" height="24" rx="12" fill="#EDE7F6"/>
  <text x="848" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#311B92" text-anchor="middle">REAL-TIME BI &amp; MCP</text>

  <!-- Left: Funil Intraday Águia Branca -->
  <g transform="translate(30, 75)" filter="url(#m3-shadow-intraday)">
    <rect width="430" height="295" rx="12" fill="#FFFFFF" stroke="#D1C4E9" stroke-width="1.5"/>
    <rect width="430" height="36" rx="12" fill="#EDE7F6"/>
    <rect y="24" width="430" height="12" fill="#EDE7F6"/>
    <text x="215" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#4527A0" text-anchor="middle">MODELAGEM INTRADAY HORÁRIA NO BIGQUERY</text>

    <text x="20" y="65" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#311B92">Tabela Gold: gld_marketing.gld_intraday_funil_model</text>
    <text x="20" y="80" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">Agregação horária (ex: "14h") para acompanhamento ágil de campanhas.</text>

    <!-- Funnel Steps Visual -->
    <g transform="translate(20, 95)">
      <rect x="0" y="0" width="390" height="28" rx="6" fill="#E8EAF6" stroke="#C5CAE9"/>
      <text x="15" y="18" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#1A237E">1. view_item</text>
      <text x="375" y="18" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368" text-anchor="end">Visualização de Passagem</text>

      <rect x="20" y="34" width="370" height="28" rx="6" fill="#C5CAE9" stroke="#9FA8DA"/>
      <text x="35" y="52" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#1A237E">2. add_to_cart</text>
      <text x="375" y="52" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368" text-anchor="end">Seleção de Poltrona</text>

      <rect x="40" y="68" width="350" height="28" rx="6" fill="#9FA8DA" stroke="#7986CB"/>
      <text x="55" y="86" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">3. begin_checkout</text>
      <text x="375" y="86" font-family="Roboto, sans-serif" font-size="9" fill="#EDE7F6" text-anchor="end">Início do Pagamento</text>

      <rect x="60" y="102" width="330" height="28" rx="6" fill="#5C6BC0" stroke="#3F51B5"/>
      <text x="75" y="120" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">4. add_contact_info</text>
      <text x="375" y="120" font-family="Roboto, sans-serif" font-size="9" fill="#E8EAF6" text-anchor="end">Identificação do Passageiro</text>

      <rect x="80" y="136" width="310" height="28" rx="6" fill="#283593"/>
      <text x="95" y="154" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">5. purchase</text>
      <text x="375" y="154" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#C5CAE9" text-anchor="end">Compra Finalizada</text>
    </g>

    <text x="20" y="280" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Segmentação: Dispositivo (mobile/desktop), source_medium, Estado e Cidade.</text>
  </g>

  <!-- Right: Observabilidade & Agentic Analytics -->
  <g transform="translate(500, 75)" filter="url(#m3-shadow-intraday)">
    <rect width="430" height="295" rx="12" fill="#FFFFFF" stroke="#B2DFDB" stroke-width="1.5"/>
    <rect width="430" height="36" rx="12" fill="#E0F2F1"/>
    <rect y="24" width="430" height="12" fill="#E0F2F1"/>
    <text x="215" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#00695C" text-anchor="middle">OBSERVABILIDADE SERVERLESS &amp; AGENTIC ANALYTICS</text>

    <!-- Block 1: Cloud Run + Slack -->
    <rect x="15" y="55" width="400" height="95" rx="8" fill="#F8F9FA" stroke="#80CBC4"/>
    <text x="25" y="75" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#004D40">Monitoramento Contínuo de Tags (Cloud Run)</text>
    <text x="25" y="92" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">• Coleta telemetria em tempo real das tags de produção</text>
    <text x="25" y="106" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">• Detecção automatizada de anomalias volumétricas e quebras de dataLayer</text>
    <text x="25" y="122" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#D32F2F">➔ Alertas instantâneos em canal do Slack via Webhooks</text>

    <!-- Block 2: Claude Code + MCP -->
    <rect x="15" y="165" width="400" height="110" rx="8" fill="#F8F9FA" stroke="#80CBC4"/>
    <text x="25" y="185" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#004D40">Agentic Analytics com Claude Code &amp; MCP</text>
    <text x="25" y="202" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">• Integração via protocolo MCP (Model Context Protocol) diretamente à API do Metabase</text>
    <text x="25" y="216" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">• Geração autônoma de consultas SQL complexas validadas na camada Gold</text>
    <text x="25" y="230" font-family="Roboto, sans-serif" font-size="9" fill="#5F6368">• Atualização programática de cards e dashboards executivos</text>
    <text x="25" y="250" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#00796B">➔ Redução drástica do tempo de entrega de relatórios e análises</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_intraday_aguiabranca.svg"), "w", encoding="utf-8") as f:
    f.write(svg_intraday)

# -----------------------------------------------------------------------------
# 6. TIM (App Meu TIM) — Mobile Telemetry & Homologação Flutter
# -----------------------------------------------------------------------------
svg_tim = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 360" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-tim" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect width="960" height="360" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="358" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#01579B"/>
  <rect x="0" y="32" width="960" height="16" fill="#01579B"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">TIM BRASIL (APP MEU TIM) — MOBILE TELEMETRY &amp; HOMOLOGAÇÃO DE SDKS FLUTTER</text>
  <rect x="790" y="12" width="146" height="24" rx="12" fill="#E1F5FE"/>
  <text x="863" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#01579B" text-anchor="middle">FIREBASE SDK &amp; ADB</text>

  <!-- 3 Workflow Steps -->
  <g transform="translate(30, 75)" filter="url(#m3-shadow-tim)">
    <rect width="280" height="260" rx="12" fill="#FFFFFF" stroke="#B3E5FC" stroke-width="1.5"/>
    <rect width="280" height="36" rx="12" fill="#E1F5FE"/>
    <rect y="24" width="280" height="12" fill="#E1F5FE"/>
    <text x="140" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#0277BD" text-anchor="middle">1. ESPECIFICAÇÃO &amp; PLANO</text>

    <rect x="12" y="55" width="256" height="60" rx="8" fill="#F8F9FA" stroke="#E1F5FE"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#01579B">Mapeamento de Jornadas</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Recarga de celular, fatura digital e PIX</text>
    <text x="22" y="102" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Contratação de Planos (Pré, Controle, Pós, Família)</text>

    <rect x="12" y="125" width="256" height="60" rx="8" fill="#F8F9FA" stroke="#E1F5FE"/>
    <text x="22" y="145" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#01579B">Migração Nativo ➔ Flutter</text>
    <text x="22" y="160" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Parceria técnica com time da Accenture</text>
    <text x="22" y="172" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Garantia de paridade de eventos de receita</text>

    <rect x="12" y="195" width="256" height="50" rx="8" fill="#E1F5FE"/>
    <text x="140" y="215" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#0277BD" text-anchor="middle">Governança ponta a ponta</text>
    <text x="140" y="230" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368" text-anchor="middle">Dicionário de dados homologado com o cliente</text>
  </g>

  <g transform="translate(340, 75)" filter="url(#m3-shadow-tim)">
    <rect width="280" height="260" rx="12" fill="#FFFFFF" stroke="#FFE082" stroke-width="1.5"/>
    <rect width="280" height="36" rx="12" fill="#FFF8E1"/>
    <rect y="24" width="280" height="12" fill="#FFF8E1"/>
    <text x="140" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#F57F17" text-anchor="middle">2. HOMOLOGAÇÃO VIA ADB</text>

    <rect x="12" y="55" width="256" height="125" rx="8" fill="#202124"/>
    <text x="22" y="75" font-family="Consolas, monospace" font-size="8.5" fill="#81C784"># Ativação de depuração Firebase</text>
    <text x="22" y="90" font-family="Consolas, monospace" font-size="8.5" fill="#E0E0E0">adb shell setprop log.tag.FA-SVC VERBOSE</text>
    <text x="22" y="105" font-family="Consolas, monospace" font-size="8.5" fill="#E0E0E0">adb shell setprop debug.firebase.app \</text>
    <text x="32" y="120" font-family="Consolas, monospace" font-size="8.5" fill="#FFF59D">br.com.timbrasil.meutim</text>
    <text x="22" y="135" font-family="Consolas, monospace" font-size="8.5" fill="#E0E0E0">adb shell setprop log.tag.GAv4 DEBUG</text>
    <text x="22" y="155" font-family="Consolas, monospace" font-size="8.5" fill="#81C784"># Filtro no Logcat: tag.FA-SVC</text>

    <rect x="12" y="190" width="256" height="55" rx="8" fill="#FFF8E1"/>
    <text x="22" y="210" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#F57F17">Validação de Payloads</text>
    <text x="22" y="225" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Inspeção de rede e parâmetros de plano e valor</text>
    <text x="22" y="237" font-family="Roboto, sans-serif" font-size="8.5" fill="#E65100">Garantia de conformidade antes da release</text>
  </g>

  <g transform="translate(650, 75)" filter="url(#m3-shadow-tim)">
    <rect width="280" height="260" rx="12" fill="#FFFFFF" stroke="#C8E6C9" stroke-width="1.5"/>
    <rect width="280" height="36" rx="12" fill="#E8F5E9"/>
    <rect y="24" width="280" height="12" fill="#E8F5E9"/>
    <text x="140" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#2E7D32" text-anchor="middle">3. MODELAGEM &amp; ATRIBUIÇÃO</text>

    <rect x="12" y="55" width="256" height="60" rx="8" fill="#F1F8E9" stroke="#C5E1A5"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#33691E">Modelos de Conversão Diária</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Acompanhamento contínuo de conversões de planos</text>
    <text x="22" y="102" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Métricas agregadas diárias e mensais do App</text>

    <rect x="12" y="125" width="256" height="60" rx="8" fill="#F1F8E9" stroke="#C5E1A5"/>
    <text x="22" y="145" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#33691E">Atribuição Play Store x GA4</text>
    <text x="22" y="160" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Mensuração do ROI de campanhas de aquisição</text>
    <text x="22" y="172" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Performance de novas features lançadas</text>

    <rect x="12" y="195" width="256" height="50" rx="8" fill="#E8F5E9"/>
    <text x="140" y="215" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#1B5E20" text-anchor="middle">Zero Discrepâncias no Go-Live</text>
    <text x="140" y="230" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368" text-anchor="middle">Transição suave para Flutter sem perda de telemetria</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_mobile_tim.svg"), "w", encoding="utf-8") as f:
    f.write(svg_tim)

# -----------------------------------------------------------------------------
# 7. CASE ACADÊMICO: BuscaRM — Aplicação Web Colaborativa Hexagonal
# -----------------------------------------------------------------------------
svg_buscarm = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-buscarm" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
    <marker id="arr-hex" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1A73E8"/>
    </marker>
  </defs>

  <rect width="960" height="420" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="418" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#1565C0"/>
  <rect x="0" y="32" width="960" height="16" fill="#1565C0"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">BUSCARM (PROJETO INTEGRADOR II - UNIVESP) — ARQUITETURA WEB HEXAGONAL &amp; OCR</text>
  <rect x="760" y="12" width="176" height="24" rx="12" fill="#BBDEFB"/>
  <text x="848" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#0D47A1" text-anchor="middle">PORTS &amp; ADAPTERS</text>

  <!-- 4 Columns / Topology Layers -->
  <!-- Col 1: Frontend Next.js 14 -->
  <g transform="translate(30, 70)" filter="url(#m3-shadow-buscarm)">
    <rect width="190" height="320" rx="12" fill="#FFFFFF" stroke="#DADCE0" stroke-width="1.5"/>
    <rect width="190" height="36" rx="12" fill="#E3F2FD"/>
    <rect y="24" width="190" height="12" fill="#E3F2FD"/>
    <text x="95" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#1565C0" text-anchor="middle">FRONTEND (NEXT.JS 14)</text>

    <rect x="12" y="55" width="166" height="65" rx="8" fill="#F8F9FA" stroke="#BBDEFB"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#0D47A1">Feature-Sliced Design</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">app ➔ features ➔ entities ➔ shared</text>
    <text x="22" y="104" font-family="Roboto, sans-serif" font-size="8.5" fill="#1976D2">React 18 · TypeScript · Vercel</text>

    <rect x="12" y="130" width="166" height="85" rx="8" fill="#F8F9FA" stroke="#BBDEFB"/>
    <text x="22" y="150" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#0D47A1">Módulos de Interface</text>
    <text x="22" y="166" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Busca instantânea Nome ➔ RM</text>
    <text x="22" y="180" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Upload drag &amp; drop de planilhas</text>
    <text x="22" y="194" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">• Pré-visualização de OCR de fotos</text>
    <text x="22" y="208" font-family="Roboto, sans-serif" font-size="8.5" fill="#137333">Validação humana antes de gravar</text>

    <rect x="12" y="225" width="166" height="80" rx="8" fill="#E3F2FD"/>
    <text x="22" y="245" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#1565C0">Segurança &amp; RBAC</text>
    <text x="22" y="260" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">JWT stateless em cabeçalhos</text>
    <text x="22" y="274" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Controle de visualização por perfil:</text>
    <text x="22" y="288" font-family="Roboto, sans-serif" font-size="8.5" font-weight="600" fill="#0D47A1">ADMIN · SECRETARIA · VISUALIZADOR</text>
  </g>

  <!-- Connector Frontend -> Backend -->
  <path d="M 220 220 L 260 220" stroke="#1A73E8" stroke-width="2" fill="none" marker-end="url(#arr-hex)"/>

  <!-- Col 2: Backend Hexagonal (Spring Boot 3.3 / Java 21) -->
  <g transform="translate(260, 70)" filter="url(#m3-shadow-buscarm)">
    <rect width="250" height="320" rx="12" fill="#FFFFFF" stroke="#C8E6C9" stroke-width="1.5"/>
    <rect width="250" height="36" rx="12" fill="#E8F5E9"/>
    <rect y="24" width="250" height="12" fill="#E8F5E9"/>
    <text x="125" y="23" font-family="Roboto, sans-serif" font-size="12" font-weight="700" fill="#2E7D32" text-anchor="middle">BACKEND HEXAGONAL (JAVA 21)</text>

    <!-- Ports & Adapters Box -->
    <rect x="12" y="55" width="226" height="75" rx="8" fill="#F1F8E9" stroke="#C5E1A5"/>
    <text x="22" y="75" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#1B5E20">Ports &amp; Adapters Pattern</text>
    <text x="22" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Domínio e regras isolados de frameworks</text>
    <text x="22" y="104" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Package-by-feature (registro, importação, segurança)</text>
    <text x="22" y="118" font-family="Roboto, sans-serif" font-size="8.5" fill="#33691E">Spring Boot 3.3 · Spring Data JPA · Flyway</text>

    <!-- Normalization & Search Engine -->
    <rect x="12" y="140" width="226" height="80" rx="8" fill="#F1F8E9" stroke="#C5E1A5"/>
    <text x="22" y="160" font-family="Roboto, sans-serif" font-size="10.5" font-weight="700" fill="#1B5E20">Busca e Normalização</text>
    <text x="22" y="176" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Indexador NomeNormalizer: minúsculas, sem acento</text>
    <text x="22" y="190" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Armazena nome_completo e nome_busca</text>
    <text x="22" y="204" font-family="Roboto, sans-serif" font-size="8.5" fill="#33691E">Busca otimizada em milissegundos sobre 6.000+ RMs</text>

    <!-- Audit & Soft Delete -->
    <rect x="12" y="230" width="226" height="70" rx="8" fill="#E8F5E9"/>
    <text x="22" y="250" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#1B5E20">Rastreabilidade &amp; Auditoria</text>
    <text x="22" y="266" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Soft deletes (ativo=false) e histórico de ações</text>
    <text x="22" y="280" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Relatório de importação com status de cada linha</text>
  </g>

  <!-- Connector Backend -> Import Pipeline & DB -->
  <path d="M 510 180 L 550 150" stroke="#1E8E3E" stroke-width="2" fill="none" marker-end="url(#arr-hex)"/>
  <path d="M 510 280 L 550 310" stroke="#1A73E8" stroke-width="2" fill="none" marker-end="url(#arr-hex)"/>

  <!-- Col 3: Pipeline de Importação Único (OCR + Excel) -->
  <g transform="translate(550, 70)" filter="url(#m3-shadow-buscarm)">
    <rect width="210" height="170" rx="12" fill="#FFFFFF" stroke="#FFE082" stroke-width="1.5"/>
    <rect width="210" height="32" rx="12" fill="#FFF8E1"/>
    <rect y="20" width="210" height="12" fill="#FFF8E1"/>
    <text x="105" y="21" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#F57F17" text-anchor="middle">PIPELINE ÚNICO DE IMPORTAÇÃO</text>

    <text x="15" y="52" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#E65100">1. Apache POI &amp; Parser CSV</text>
    <text x="15" y="66" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Leitura robusta de .xlsx e .csv (RFC 4180)</text>

    <text x="15" y="88" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#E65100">2. Tesseract OCR Nativo (CLI)</text>
    <text x="15" y="102" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">ProcessBuilder, LSTM neural net, --psm 3</text>
    <text x="15" y="116" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Extração de RM e nomes de fotos de livros</text>

    <rect x="10" y="128" width="190" height="32" rx="6" fill="#FFF8E1"/>
    <text x="105" y="143" font-family="Roboto, sans-serif" font-size="8.5" font-weight="700" fill="#F57F17" text-anchor="middle">Validador de Negócio Compartilhado</text>
    <text x="105" y="154" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">VÁLIDO · INVÁLIDO · DUPLICADO · CONFLITO</text>
  </g>

  <!-- Col 4: Banco PostgreSQL Neon & Infra -->
  <g transform="translate(550, 260)" filter="url(#m3-shadow-buscarm)">
    <rect width="210" height="130" rx="12" fill="#FFFFFF" stroke="#90CAF9" stroke-width="1.5"/>
    <rect width="210" height="32" rx="12" fill="#E3F2FD"/>
    <rect y="20" width="210" height="12" fill="#E3F2FD"/>
    <text x="105" y="21" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#1565C0" text-anchor="middle">BANCO POSTGRESQL &amp; DEPLOY</text>

    <text x="15" y="55" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#0D47A1">PostgreSQL Serverless (Neon)</text>
    <text x="15" y="70" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Índices específicos para busca de texto</text>
    <text x="15" y="88" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#0D47A1">CI/CD &amp; Contêineres</text>
    <text x="15" y="103" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Docker · GitHub Actions · GHCR · Render</text>
  </g>

  <!-- Impact summary right side -->
  <g transform="translate(780, 70)" filter="url(#m3-shadow-buscarm)">
    <rect width="150" height="320" rx="12" fill="#FFFFFF" stroke="#B0BEC5" stroke-width="1.5"/>
    <rect width="150" height="36" rx="12" fill="#ECEFF1"/>
    <rect y="24" width="150" height="12" fill="#ECEFF1"/>
    <text x="75" y="23" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#37474F" text-anchor="middle">IMPACTO REAL</text>

    <rect x="10" y="55" width="130" height="75" rx="8" fill="#F8F9FA"/>
    <text x="15" y="75" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#263238">Redução de Tempo</text>
    <text x="15" y="90" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">De 15+ min folheando</text>
    <text x="15" y="103" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">livro físico para busca</text>
    <text x="15" y="116" font-family="Roboto, sans-serif" font-size="8.5" font-weight="700" fill="#2E7D32">em &lt; 2 segundos.</text>

    <rect x="10" y="140" width="130" height="80" rx="8" fill="#F8F9FA"/>
    <text x="15" y="160" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#263238">Fim de Perda de RMs</text>
    <text x="15" y="175" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">Garantia de integridade</text>
    <text x="15" y="188" font-family="Roboto, sans-serif" font-size="8.5" fill="#5F6368">histórica e digitalização</text>
    <text x="15" y="201" font-family="Roboto, sans-serif" font-size="8.5" font-weight="700" fill="#2E7D32">do acervo da escola.</text>

    <rect x="10" y="230" width="130" height="75" rx="8" fill="#ECEFF1"/>
    <text x="75" y="255" font-family="Roboto, sans-serif" font-size="9" font-weight="700" fill="#37474F" text-anchor="middle">Metodologia Ágil</text>
    <text x="75" y="270" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Validação colaborativa</text>
    <text x="75" y="282" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">com secretárias escolares</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_buscarm_academic.svg"), "w", encoding="utf-8") as f:
    f.write(svg_buscarm)

# -----------------------------------------------------------------------------
# 8. CASE ACADÊMICO: Mineração de Dados & Framework KDD + CRISP-DM
# -----------------------------------------------------------------------------
svg_mining = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" width="100%" height="100%">
  <defs>
    <filter id="m3-shadow-mining" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
    <marker id="arr-kdd" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1565C0"/>
    </marker>
  </defs>

  <rect width="960" height="400" rx="16" fill="#F8F9FA"/>
  <rect x="1" y="1" width="958" height="398" rx="15" fill="none" stroke="#E0E0E0" stroke-width="1.5"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="960" height="48" rx="16" fill="#00695C"/>
  <rect x="0" y="32" width="960" height="16" fill="#00695C"/>
  <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF">MINERAÇÃO DE DADOS (COM360) — MAPA METODOLÓGICO KDD &amp; CICLO CRISP-DM</text>
  <rect x="760" y="12" width="176" height="24" rx="12" fill="#E0F2F1"/>
  <text x="848" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#00695C" text-anchor="middle">CIÊNCIA DE DADOS APLICADA</text>

  <!-- KDD Linear Pipeline (Top) -->
  <g transform="translate(30, 70)" filter="url(#m3-shadow-mining)">
    <rect width="900" height="135" rx="12" fill="#FFFFFF" stroke="#B2DFDB" stroke-width="1.5"/>
    <rect width="900" height="30" rx="12" fill="#E0F2F1"/>
    <rect y="18" width="900" height="12" fill="#E0F2F1"/>
    <text x="20" y="20" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#004D40">FRAMEWORK KDD (KNOWLEDGE DISCOVERY IN DATABASES) — FLUXO TÉCNICO E CIENTÍFICO</text>

    <!-- KDD Steps -->
    <g transform="translate(20, 45)">
      <!-- Step 1: Raw Data -->
      <rect x="0" y="0" width="150" height="70" rx="8" fill="#F8F9FA" stroke="#DADCE0"/>
      <text x="75" y="20" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#202124" text-anchor="middle">1. Dados Brutos (Raw)</text>
      <text x="75" y="36" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Bases transacionais, CSVs,</text>
      <text x="75" y="48" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">CRM &amp; Eventos Web</text>
      <text x="75" y="62" font-family="Roboto, sans-serif" font-size="8" font-weight="700" fill="#1967D2" text-anchor="middle">Camada Bronze</text>

      <path d="M 152 35 L 175 35" stroke="#1565C0" stroke-width="2" marker-end="url(#arr-kdd)"/>

      <!-- Step 2: Pré-processamento -->
      <rect x="180" y="0" width="165" height="70" rx="8" fill="#E8F0FE" stroke="#AECBFA"/>
      <text x="262" y="20" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#1565C0" text-anchor="middle">2. Pré-processamento</text>
      <text x="262" y="35" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">Tratamento de incompletude (imputação)</text>
      <text x="262" y="47" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">Remoção de ruídos &amp; outliers (IQR)</text>
      <text x="262" y="62" font-family="Roboto, sans-serif" font-size="8" font-weight="700" fill="#1967D2" text-anchor="middle">Camada Silver</text>

      <path d="M 347 35 L 370 35" stroke="#1565C0" stroke-width="2" marker-end="url(#arr-kdd)"/>

      <!-- Step 3: Transformação -->
      <rect x="375" y="0" width="160" height="70" rx="8" fill="#F3E5F5" stroke="#CE93D8"/>
      <text x="455" y="20" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#7B1FA2" text-anchor="middle">3. Transformação &amp; Redução</text>
      <text x="455" y="35" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">Normalização (Z-Score, Min-Max)</text>
      <text x="455" y="47" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">Discretização (Binning), PCA</text>
      <text x="455" y="62" font-family="Roboto, sans-serif" font-size="8" font-weight="700" fill="#7B1FA2" text-anchor="middle">Engenharia de Atributos</text>

      <path d="M 537 35 L 560 35" stroke="#1565C0" stroke-width="2" marker-end="url(#arr-kdd)"/>

      <!-- Step 4: Mineração de Dados -->
      <rect x="565" y="0" width="150" height="70" rx="8" fill="#FFF8E1" stroke="#FFE082"/>
      <text x="640" y="20" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#B78103" text-anchor="middle">4. Mineração de Dados</text>
      <text x="640" y="35" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">Algoritmos de classificação,</text>
      <text x="640" y="47" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">agrupamento, regressão</text>
      <text x="640" y="62" font-family="Roboto, sans-serif" font-size="8" font-weight="700" fill="#B78103" text-anchor="middle">Modelos Preditivos / Gold</text>

      <path d="M 717 35 L 740 35" stroke="#1565C0" stroke-width="2" marker-end="url(#arr-kdd)"/>

      <!-- Step 5: Conhecimento -->
      <rect x="745" y="0" width="115" height="70" rx="8" fill="#E8F5E9" stroke="#A5D6A7"/>
      <text x="802" y="20" font-family="Roboto, sans-serif" font-size="10" font-weight="700" fill="#2E7D32" text-anchor="middle">5. Conhecimento</text>
      <text x="802" y="35" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">Padrões válidos,</text>
      <text x="802" y="47" font-family="Roboto, sans-serif" font-size="8" fill="#3C4043" text-anchor="middle">KPIs acionáveis</text>
      <text x="802" y="62" font-family="Roboto, sans-serif" font-size="8" font-weight="700" fill="#2E7D32" text-anchor="middle">Valor Estratégico</text>
    </g>
  </g>

  <!-- CRISP-DM Cycle (Bottom) -->
  <g transform="translate(30, 220)" filter="url(#m3-shadow-mining)">
    <rect width="900" height="155" rx="12" fill="#FFFFFF" stroke="#D7CCC8" stroke-width="1.5"/>
    <rect width="900" height="30" rx="12" fill="#EFEBE9"/>
    <rect y="18" width="900" height="12" fill="#EFEBE9"/>
    <text x="20" y="20" font-family="Roboto, sans-serif" font-size="11" font-weight="700" fill="#4E342E">METODOLOGIA CRISP-DM — CICLO DE VALOR DE NEGÓCIO APLICADO AO ANALYTICS</text>

    <!-- CRISP-DM 6 Pillars Grid -->
    <g transform="translate(15, 45)">
      <!-- 1. Business Understanding -->
      <rect x="0" y="0" width="138" height="95" rx="8" fill="#F8F9FA" stroke="#E0E0E0"/>
      <text x="69" y="18" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#202124" text-anchor="middle">1. Business Und.</text>
      <text x="69" y="34" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Definição de metas,</text>
      <text x="69" y="46" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">OKRs, regras de negócio</text>
      <text x="69" y="58" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">e critérios de sucesso.</text>
      <text x="69" y="78" font-family="Roboto, sans-serif" font-size="8" font-weight="600" fill="#1A73E8" text-anchor="middle">Ex: CAC, LTV, ROAS</text>

      <!-- 2. Data Understanding -->
      <rect x="146" y="0" width="138" height="95" rx="8" fill="#F8F9FA" stroke="#E0E0E0"/>
      <text x="215" y="18" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#202124" text-anchor="middle">2. Data Und.</text>
      <text x="215" y="34" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Auditoria de tracking,</text>
      <text x="215" y="46" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">identificação de gaps,</text>
      <text x="215" y="58" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">EDA e distribuições.</text>
      <text x="215" y="78" font-family="Roboto, sans-serif" font-size="8" font-weight="600" fill="#1A73E8" text-anchor="middle">Ex: Quebras de UTM</text>

      <!-- 3. Data Preparation -->
      <rect x="292" y="0" width="138" height="95" rx="8" fill="#F8F9FA" stroke="#E0E0E0"/>
      <text x="361" y="18" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#202124" text-anchor="middle">3. Data Preparation</text>
      <text x="361" y="34" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Pipelines ELT, limpeza,</text>
      <text x="361" y="46" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">deduplicação de chaves</text>
      <text x="361" y="58" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">e modelagem tabular.</text>
      <text x="361" y="78" font-family="Roboto, sans-serif" font-size="8" font-weight="600" fill="#1A73E8" text-anchor="middle">Ex: Dataform SQLX</text>

      <!-- 4. Modeling -->
      <rect x="438" y="0" width="138" height="95" rx="8" fill="#F8F9FA" stroke="#E0E0E0"/>
      <text x="507" y="18" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#202124" text-anchor="middle">4. Modeling</text>
      <text x="507" y="34" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Modelos analíticos,</text>
      <text x="507" y="46" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">funis intraday e</text>
      <text x="507" y="58" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">algoritmos de ML.</text>
      <text x="507" y="78" font-family="Roboto, sans-serif" font-size="8" font-weight="600" fill="#1A73E8" text-anchor="middle">Ex: Funil Águia Branca</text>

      <!-- 5. Evaluation -->
      <rect x="584" y="0" width="138" height="95" rx="8" fill="#F8F9FA" stroke="#E0E0E0"/>
      <text x="653" y="18" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#202124" text-anchor="middle">5. Evaluation</text>
      <text x="653" y="34" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Reconciliação diária,</text>
      <text x="653" y="46" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">validação cruzada k-fold</text>
      <text x="653" y="58" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">e assertions de negócio.</text>
      <text x="653" y="78" font-family="Roboto, sans-serif" font-size="8" font-weight="600" fill="#137333" text-anchor="middle">Ex: Paridade &gt;98%</text>

      <!-- 6. Deployment -->
      <rect x="730" y="0" width="138" height="95" rx="8" fill="#E8F5E9" stroke="#C8E6C9"/>
      <text x="799" y="18" font-family="Roboto, sans-serif" font-size="9.5" font-weight="700" fill="#1B5E20" text-anchor="middle">6. Deployment</text>
      <text x="799" y="34" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Dashboards Metabase,</text>
      <text x="799" y="46" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">Tags GTM em produção,</text>
      <text x="799" y="58" font-family="Roboto, sans-serif" font-size="8" fill="#5F6368" text-anchor="middle">alertas no Slack.</text>
      <text x="799" y="78" font-family="Roboto, sans-serif" font-size="8" font-weight="700" fill="#2E7D32" text-anchor="middle">Ex: Cloud Run + MCP</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "architecture_kdd_crispdm_mining.svg"), "w", encoding="utf-8") as f:
    f.write(svg_mining)

print("ALL 7 DIAGRAMS GENERATED SUCCESSFULLY IN:", assets_dir)
