# -*- coding: utf-8 -*-
"""Legal notice and privacy policy bodies. Missing facts are marked 【待补】."""

TODO = '<mark class="todo-gap">【待补】</mark>'
GH_ADDR = "GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States"
HOLDING = "FLAT/RM 617A 6/F, GLOBAL PLAZA NO. 1, SHA TSUI ROAD, TSUEN WAN, HONG KONG"
COMPANY = "Hong Kong Bright Bridge Group Co., Limited"
PRIVACY_MAIL = "ohashi@brightbridgegroup.com"
QUOTE_MAIL = "ohashi@brightbridgegroup.com"
CC_MAIL = "ikkei@brightbridgegroup.com"
GH_PRIVACY = "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement"


def _todo():
    return TODO


def legal_body(lang: str) -> str:
    t = _todo()
    if lang == "en":
        return f"""
<h2>Publisher</h2>
<p>This website is published by {COMPANY}, which uses the brand AuraBridge.</p>
<p>Registered office: {HOLDING}</p>
<p>Legal form: a company limited by shares under the laws of Hong Kong.</p>
<p>Company registration number: {t}</p>
<p>Share capital: {t}</p>
<p>VAT number: {t}</p>
<p>Contact e-mail: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Telephone: <a href="tel:+8676989399795">+86 769 8939 9795</a></p>
<h2>Director of publication</h2>
<p>The director of publication (<span lang="fr">directeur de la publication</span>) is: {t}</p>
<h2>Host</h2>
<p>This website is hosted on GitHub Pages, operated by {GH_ADDR}.</p>
<p>Websites: <a href="https://github.com">https://github.com</a> and <a href="https://pages.github.com">https://pages.github.com</a>.</p>
<h2>Intellectual property</h2>
<p>The AuraBridge name, the logo and the content of this website are protected. They may not be copied for commercial use without permission.</p>
"""
    if lang == "zh":
        return f"""
<h2>发布者</h2>
<p>本网站由 {COMPANY} 发布，使用品牌名称 AuraBridge。</p>
<p>注册地址：{HOLDING}</p>
<p>法律形式：根据香港法律设立的有限公司。</p>
<p>公司注册号：{t}</p>
<p>股本：{t}</p>
<p>增值税号：{t}</p>
<p>联系邮箱：<a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>电话：<a href="tel:+8676989399795">+86 769 8939 9795</a></p>
<h2>出版负责人</h2>
<p>出版负责人（directeur de la publication）为：{t}</p>
<h2>托管方</h2>
<p>本网站托管于 GitHub Pages，运营方为 {GH_ADDR}。</p>
<p>网站：<a href="https://github.com">https://github.com</a> 与 <a href="https://pages.github.com">https://pages.github.com</a>。</p>
<h2>知识产权</h2>
<p>AuraBridge 名称、标识及本网站内容受保护，未经许可不得用于商业复制。</p>
"""
    if lang == "fr":
        return f"""
<h2>Éditeur</h2>
<p>Le présent site est édité par {COMPANY}, qui exploite la marque AuraBridge.</p>
<p>Siège social : {HOLDING}</p>
<p>Forme juridique : société de type « company limited by shares » de droit de Hong Kong.</p>
<p>Numéro d’immatriculation : {t}</p>
<p>Capital social : {t}</p>
<p>Numéro de TVA : {t}</p>
<p>Courriel de contact : <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Téléphone : <a href="tel:+8676989399795">+86 769 8939 9795</a></p>
<h2>Directeur de la publication</h2>
<p>Le directeur de la publication est : {t}</p>
<h2>Hébergeur</h2>
<p>Le site est hébergé par GitHub Pages, service opéré par {GH_ADDR}.</p>
<p>Sites : <a href="https://github.com">https://github.com</a> et <a href="https://pages.github.com">https://pages.github.com</a>.</p>
<h2>Propriété intellectuelle</h2>
<p>Le nom AuraBridge, le logo et les contenus de ce site sont protégés. Ils ne peuvent pas être reproduits à des fins commerciales sans autorisation.</p>
"""
    if lang == "de":
        return f"""
<h2>Herausgeber</h2>
<p>Diese Website wird herausgegeben von {COMPANY}, unter der Marke AuraBridge.</p>
<p>Sitz: {HOLDING}</p>
<p>Rechtsform: eine Gesellschaft mit beschränkter Haftung nach dem Recht von Hongkong (company limited by shares).</p>
<p>Handelsregisternummer: {t}</p>
<p>Stammkapital: {t}</p>
<p>Umsatzsteuer-Identifikationsnummer: {t}</p>
<p>Kontakt-E-Mail: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Telefon: <a href="tel:+8676989399795">+86 769 8939 9795</a></p>
<h2>Verantwortlicher der Veröffentlichung</h2>
<p>Der Verantwortliche der Veröffentlichung (directeur de la publication) ist: {t}</p>
<h2>Hosting</h2>
<p>Die Website wird über GitHub Pages bereitgestellt, betrieben von {GH_ADDR}.</p>
<p>Websites: <a href="https://github.com">https://github.com</a> und <a href="https://pages.github.com">https://pages.github.com</a>.</p>
<h2>Geistiges Eigentum</h2>
<p>Der Name AuraBridge, das Logo und die Inhalte dieser Website sind geschützt. Eine kommerzielle Vervielfältigung ist ohne Erlaubnis nicht gestattet.</p>
"""
    # es
    return f"""
<h2>Editor</h2>
<p>Este sitio lo publica {COMPANY}, que utiliza la marca AuraBridge.</p>
<p>Domicilio social: {HOLDING}</p>
<p>Forma jurídica: sociedad de responsabilidad limitada (company limited by shares) conforme al Derecho de Hong Kong.</p>
<p>Número de inscripción: {t}</p>
<p>Capital social: {t}</p>
<p>Número de IVA: {t}</p>
<p>Correo de contacto: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Teléfono: <a href="tel:+8676989399795">+86 769 8939 9795</a></p>
<h2>Director de la publicación</h2>
<p>El director de la publicación (directeur de la publication) es: {t}</p>
<h2>Alojamiento</h2>
<p>Este sitio está alojado en GitHub Pages, operado por {GH_ADDR}.</p>
<p>Sitios: <a href="https://github.com">https://github.com</a> y <a href="https://pages.github.com">https://pages.github.com</a>.</p>
<h2>Propiedad intelectual</h2>
<p>El nombre AuraBridge, el logotipo y los contenidos de este sitio están protegidos. No pueden copiarse para uso comercial sin autorización.</p>
"""


def privacy_body(lang: str) -> str:
    t = _todo()
    if lang == "en":
        return f"""
<h2>Who is responsible</h2>
<p>The organisation responsible for personal data received through this website is {COMPANY}, {HOLDING}.</p>
<p>Privacy contact: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>European Union representative under Article 27 GDPR, if one is required: {t}</p>
<h2>This site does not use cookies or trackers</h2>
<p>This website does not set cookies, does not use local storage, and does not load analytics, advertising, social plugins, maps, or third-party font or script services. Fonts are hosted on this website. No cookie banner is shown, because the site itself does not deposit cookies.</p>
<h2>Hosting</h2>
<p>The site is hosted by GitHub, Inc. (GitHub Pages) in the United States. When you visit these pages, the host may process technical data such as IP addresses and server logs, under GitHub’s own terms and <a href="{GH_PRIVACY}">privacy statement</a>.</p>
<p>We do not operate a user-account system on this site.</p>
<h2>Quote form</h2>
<p>The “Request a quote” form does not send your data to a server on this website and does not store it in a database here. After you complete the required fields, your email application opens with a pre-filled message. The message is sent only if you send it yourself.</p>
<p>If you send that email, we receive:</p>
<ul>
<li>your name;</li>
<li>your email address;</li>
<li>your company name, if you entered one;</li>
<li>the product you selected;</li>
<li>your message.</li>
</ul>
<p>The email is sent to <a href="mailto:{QUOTE_MAIL}">{QUOTE_MAIL}</a>, and a copy is addressed to <a href="mailto:{CC_MAIL}">{CC_MAIL}</a>.</p>
<p>Purpose: to reply to your request for a wholesale quote or a sample, and to follow up on that request.</p>
<p>Legal basis: taking steps at your request before entering into a contract (Article 6(1)(b) of the GDPR).</p>
<p>How long we keep the email: {t}</p>
<p>We do not sell this data. It is used by {COMPANY} to handle your request. Because the company is in Hong Kong, the content of your email is received outside the European Economic Area. The safeguard used for that transfer, if applicable: {t}</p>
<h2>Your rights</h2>
<p>You may ask to access, correct or delete your personal data, to restrict or object to certain processing, and, where applicable, to receive your data in a portable form. To exercise these rights, write to <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>.</p>
<p>You may also lodge a complaint with a supervisory authority. In France, this is the CNIL (<a href="https://www.cnil.fr">https://www.cnil.fr</a>). If you live in another EU or EEA country, you may contact your local authority.</p>
<h2>Changes</h2>
<p>If this policy changes, we will update this page and the date shown at the top.</p>
"""
    if lang == "zh":
        return f"""
<h2>责任方</h2>
<p>通过本网站收到的个人数据，由 {COMPANY} 负责处理，地址为 {HOLDING}。</p>
<p>隐私联系邮箱：<a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>如需根据《通用数据保护条例》（GDPR）第 27 条指定的欧盟代表：{t}</p>
<h2>本站不使用 cookie 或追踪工具</h2>
<p>本网站不设置 cookie，不使用本地存储（localStorage），也不加载分析、广告、社交插件、地图，或第三方字体与脚本服务。字体由本站自行托管。因为本站本身不存放 cookie，所以不显示 cookie 横幅。</p>
<h2>托管</h2>
<p>本站由位于美国的 GitHub, Inc.（GitHub Pages）托管。您访问页面时，托管方可能根据其自身条款和<a href="{GH_PRIVACY}">隐私声明</a>处理 IP 地址和服务器日志等技术数据。</p>
<p>本站不提供用户账户系统。</p>
<h2>报价表单</h2>
<p>“索取报价”表单不会把您的数据发送到本网站的服务器，也不会在此存入数据库。您填完必填项后，会打开您的邮件应用并填好草稿。只有在您本人点击发送后，邮件才会寄出。</p>
<p>如果您发送该邮件，我们会收到：</p>
<ul>
<li>姓名；</li>
<li>电子邮箱；</li>
<li>若您填写了公司名称，则还包括公司名称；</li>
<li>您选择的产品；</li>
<li>您的留言。</li>
</ul>
<p>邮件发送至 <a href="mailto:{QUOTE_MAIL}">{QUOTE_MAIL}</a>，并抄送 <a href="mailto:{CC_MAIL}">{CC_MAIL}</a>。</p>
<p>用途：回复您的批发报价或样品请求，并对该请求进行跟进。</p>
<p>法律依据：应您的请求，在订立合同前采取步骤（GDPR 第 6 条第 1 款 b 项）。</p>
<p>邮件保存期限：{t}</p>
<p>我们不会出售这些数据。数据由 {COMPANY} 用于处理您的请求。因公司位于香港，邮件内容会在欧洲经济区以外接收。如适用，该跨境传输所采用的保障措施：{t}</p>
<h2>您的权利</h2>
<p>您可以请求访问、更正或删除您的个人数据，限制或反对某些处理，并在适用情况下以可携形式获取数据。行使上述权利，请写信至 <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>。</p>
<p>您也可以向监管机构投诉。在法国，该机构为 CNIL（<a href="https://www.cnil.fr">https://www.cnil.fr</a>）。如您居住在其他欧盟或欧洲经济区国家，可联系当地监管机构。</p>
<h2>变更</h2>
<p>如本政策有变更，我们将更新本页及页首日期。</p>
"""
    if lang == "fr":
        return f"""
<h2>Responsable du traitement</h2>
<p>Le responsable du traitement des données personnelles reçues via ce site est {COMPANY}, {HOLDING}.</p>
<p>Contact confidentialité : <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Représentant dans l’Union européenne au titre de l’article 27 du RGPD, s’il est requis : {t}</p>
<h2>Ce site n’utilise ni cookies ni traceurs</h2>
<p>Ce site ne dépose pas de cookies, n’utilise pas le stockage local (localStorage) et ne charge ni outil d’analyse, ni publicité, ni module social, ni carte, ni service tiers de polices ou de scripts. Les polices sont hébergées sur ce site. Aucun bandeau de cookies n’est affiché, car le site lui-même ne dépose pas de cookies.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub, Inc. (GitHub Pages) aux États-Unis. Lorsque vous consultez les pages, l’hébergeur peut traiter des données techniques telles que des adresses IP et des journaux de serveur, selon ses propres conditions et sa <a href="{GH_PRIVACY}">déclaration de confidentialité</a>.</p>
<p>Nous n’exploitons pas de comptes utilisateurs sur ce site.</p>
<h2>Formulaire de devis</h2>
<p>Le formulaire « Demander un devis » n’envoie pas vos données vers un serveur de ce site et ne les enregistre pas dans une base ici. Après saisie des champs obligatoires, votre messagerie s’ouvre avec un message prérempli. Le message n’est envoyé que si vous l’expédiez vous-même.</p>
<p>Si vous envoyez cet e-mail, nous recevons :</p>
<ul>
<li>votre nom ;</li>
<li>votre adresse e-mail ;</li>
<li>le nom de votre société, si vous l’avez indiqué ;</li>
<li>le produit choisi ;</li>
<li>votre message.</li>
</ul>
<p>L’e-mail est envoyé à <a href="mailto:{QUOTE_MAIL}">{QUOTE_MAIL}</a>, avec copie à <a href="mailto:{CC_MAIL}">{CC_MAIL}</a>.</p>
<p>Finalité : répondre à votre demande de devis de gros ou d’échantillon, et assurer le suivi de cette demande.</p>
<p>Base juridique : l’exécution de mesures précontractuelles prises à votre demande (article 6, paragraphe 1, point b, du RGPD).</p>
<p>Durée de conservation de l’e-mail : {t}</p>
<p>Nous ne vendons pas ces données. Elles sont utilisées par {COMPANY} pour traiter votre demande. Comme la société est établie à Hong Kong, le contenu de votre e-mail est reçu hors de l’Espace économique européen. Garantie utilisée pour ce transfert, le cas échéant : {t}</p>
<h2>Vos droits</h2>
<p>Vous pouvez demander l’accès, la rectification ou l’effacement de vos données, la limitation du traitement ou vous y opposer, et, le cas échéant, la portabilité de vos données. Pour exercer ces droits, écrivez à <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>.</p>
<p>Vous pouvez également introduire une réclamation auprès d’une autorité de contrôle. En France, il s’agit de la CNIL (<a href="https://www.cnil.fr">https://www.cnil.fr</a>). Si vous résidez dans un autre État de l’UE ou de l’EEE, vous pouvez saisir l’autorité locale.</p>
<h2>Modifications</h2>
<p>En cas de modification de cette politique, nous mettrons à jour cette page et la date indiquée en tête.</p>
"""
    if lang == "de":
        return f"""
<h2>Verantwortliche Stelle</h2>
<p>Verantwortlich für personenbezogene Daten, die über diese Website eingehen, ist {COMPANY}, {HOLDING}.</p>
<p>Kontakt für Datenschutz: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Vertreter in der Europäischen Union nach Artikel 27 DSGVO, sofern erforderlich: {t}</p>
<h2>Diese Website verwendet keine Cookies oder Tracker</h2>
<p>Diese Website setzt keine Cookies, nutzt keinen lokalen Speicher (localStorage) und lädt keine Analyse-, Werbe- oder Social-Plugins, keine Karten und keine Schrift- oder Skriptdienste Dritter. Die Schriften werden auf dieser Website gehostet. Es wird kein Cookie-Banner angezeigt, weil die Website selbst keine Cookies setzt.</p>
<h2>Hosting</h2>
<p>Die Website wird von GitHub, Inc. (GitHub Pages) in den Vereinigten Staaten gehostet. Beim Aufruf der Seiten kann der Host technische Daten wie IP-Adressen und Serverprotokolle nach seinen eigenen Bedingungen und seiner <a href="{GH_PRIVACY}">Datenschutzerklärung</a> verarbeiten.</p>
<p>Wir betreiben auf dieser Website kein Nutzerkontosystem.</p>
<h2>Angebotsformular</h2>
<p>Das Formular „Angebot anfordern“ sendet Ihre Daten nicht an einen Server dieser Website und speichert sie hier nicht in einer Datenbank. Nach dem Ausfüllen der Pflichtfelder öffnet sich Ihr E-Mail-Programm mit einer vorausgefüllten Nachricht. Die Nachricht wird nur gesendet, wenn Sie sie selbst absenden.</p>
<p>Wenn Sie diese E-Mail senden, erhalten wir:</p>
<ul>
<li>Ihren Namen;</li>
<li>Ihre E-Mail-Adresse;</li>
<li>Ihren Unternehmensnamen, sofern Sie ihn angegeben haben;</li>
<li>das ausgewählte Produkt;</li>
<li>Ihre Nachricht.</li>
</ul>
<p>Die E-Mail geht an <a href="mailto:{QUOTE_MAIL}">{QUOTE_MAIL}</a>, eine Kopie an <a href="mailto:{CC_MAIL}">{CC_MAIL}</a>.</p>
<p>Zweck: Beantwortung Ihrer Anfrage zu einem Großhandelsangebot oder Muster und die weitere Bearbeitung dieser Anfrage.</p>
<p>Rechtsgrundlage: Durchführung vorvertraglicher Maßnahmen auf Ihre Anfrage (Artikel 6 Absatz 1 Buchstabe b DSGVO).</p>
<p>Speicherdauer der E-Mail: {t}</p>
<p>Wir verkaufen diese Daten nicht. Sie werden von {COMPANY} zur Bearbeitung Ihrer Anfrage verwendet. Da das Unternehmen in Hongkong ansässig ist, geht der Inhalt Ihrer E-Mail außerhalb des Europäischen Wirtschaftsraums ein. Die gegebenenfalls verwendete Garantie für diese Übermittlung: {t}</p>
<h2>Ihre Rechte</h2>
<p>Sie können Auskunft, Berichtigung oder Löschung Ihrer Daten verlangen, die Verarbeitung einschränken oder ihr widersprechen und, soweit einschlägig, die Daten in einem übertragbaren Format erhalten. Zur Ausübung dieser Rechte schreiben Sie an <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>.</p>
<p>Sie können auch eine Beschwerde bei einer Aufsichtsbehörde einlegen. In Frankreich ist dies die CNIL (<a href="https://www.cnil.fr">https://www.cnil.fr</a>). Wenn Sie in einem anderen EU- oder EWR-Staat leben, können Sie sich an die dortige Behörde wenden.</p>
<h2>Änderungen</h2>
<p>Bei Änderungen dieser Erklärung aktualisieren wir diese Seite und das Datum oben.</p>
"""
    return f"""
<h2>Responsable</h2>
<p>El responsable de los datos personales recibidos a través de este sitio es {COMPANY}, {HOLDING}.</p>
<p>Contacto de privacidad: <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a></p>
<p>Representante en la Unión Europea conforme al artículo 27 del RGPD, si se requiere: {t}</p>
<h2>Este sitio no usa cookies ni rastreadores</h2>
<p>Este sitio no instala cookies, no usa almacenamiento local (localStorage) y no carga analítica, publicidad, complementos sociales, mapas ni servicios de fuentes o scripts de terceros. Las fuentes están alojadas en este sitio. No se muestra un banner de cookies porque el propio sitio no deposita cookies.</p>
<h2>Alojamiento</h2>
<p>El sitio está alojado por GitHub, Inc. (GitHub Pages) en Estados Unidos. Al visitar las páginas, el anfitrión puede tratar datos técnicos como direcciones IP y registros del servidor, de acuerdo con sus propias condiciones y su <a href="{GH_PRIVACY}">declaración de privacidad</a>.</p>
<p>No operamos un sistema de cuentas de usuario en este sitio.</p>
<h2>Formulario de presupuesto</h2>
<p>El formulario «Solicitar un presupuesto» no envía sus datos a un servidor de este sitio ni los guarda aquí en una base de datos. Tras completar los campos obligatorios, se abre su aplicación de correo con un mensaje prediligenciado. El mensaje solo se envía si usted lo envía.</p>
<p>Si envía ese correo, recibimos:</p>
<ul>
<li>su nombre;</li>
<li>su correo electrónico;</li>
<li>el nombre de su empresa, si lo ha indicado;</li>
<li>el producto seleccionado;</li>
<li>su mensaje.</li>
</ul>
<p>El correo se envía a <a href="mailto:{QUOTE_MAIL}">{QUOTE_MAIL}</a>, con copia a <a href="mailto:{CC_MAIL}">{CC_MAIL}</a>.</p>
<p>Finalidad: responder a su solicitud de presupuesto mayorista o de muestra, y hacer el seguimiento de esa solicitud.</p>
<p>Base jurídica: adopción de medidas precontractuales a petición suya (artículo 6, apartado 1, letra b, del RGPD).</p>
<p>Plazo de conservación del correo: {t}</p>
<p>No vendemos estos datos. Los utiliza {COMPANY} para tramitar su solicitud. Como la empresa está en Hong Kong, el contenido de su correo se recibe fuera del Espacio Económico Europeo. La garantía utilizada para esa transferencia, si procede: {t}</p>
<h2>Sus derechos</h2>
<p>Puede solicitar el acceso, la rectificación o la supresión de sus datos, la limitación u oposición a determinados tratamientos y, cuando proceda, recibir sus datos en un formato portátil. Para ejercer estos derechos, escriba a <a href="mailto:{PRIVACY_MAIL}">{PRIVACY_MAIL}</a>.</p>
<p>También puede presentar una reclamación ante una autoridad de control. En Francia, es la CNIL (<a href="https://www.cnil.fr">https://www.cnil.fr</a>). Si vive en otro país de la UE o del EEE, puede dirigirse a la autoridad local.</p>
<h2>Cambios</h2>
<p>Si esta política cambia, actualizaremos esta página y la fecha que aparece al inicio.</p>
"""
