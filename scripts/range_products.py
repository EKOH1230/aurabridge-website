# -*- coding: utf-8 -*-
"""Copy and image data for the models added to the range in November 2026.

Specs come only from the supplier quote of 27 Nov 2026. Anything the quote
does not state is written as "available on request". No prices, minimum
orders, certification marks, or treatment claims appear here.
"""

LABELS = {
    "en": {"material": "Material", "dims": "Dimensions", "weight": "Net weight", "battery": "Battery", "charging": "Charging", "power": "Power", "reservoir": "Reservoir", "colour": "Standard colour", "magnif": "Magnification", "image": "Image", "conn": "Connection", "app": "App", "light": "Light", "modes": "Modes", "water": "Water resistance", "runtime": "Use time", "heads": "Heads", "type": "Type", "dispense": "Dispensing", "massage": "Massage", "mist": "Mist", "liquids": "Liquids", "motor": "Motor speed", "bristles": "Bristles", "plate": "Brush plate", "autooff": "Auto-off", "dosing": "Dosing chamber", "tips": "Tips", "suction": "Suction", "base": "Base", "vibration": "Vibration"},
    "zh": {"material": "材质", "dims": "尺寸", "weight": "净重", "battery": "电池", "charging": "充电", "power": "功率", "reservoir": "储液仓", "colour": "标准颜色", "magnif": "放大倍率", "image": "图像", "conn": "连接", "app": "应用", "light": "灯光", "modes": "档位", "water": "防水", "runtime": "使用时间", "heads": "刷头", "type": "类型", "dispense": "出液方式", "massage": "按摩", "mist": "出雾", "liquids": "适用液体", "motor": "转速", "bristles": "刷毛", "plate": "齿盘", "autooff": "自动关机", "dosing": "定量仓", "tips": "涂抹头", "suction": "吸力", "base": "底座", "vibration": "振动"},
    "fr": {"material": "Matériaux", "dims": "Dimensions", "weight": "Poids net", "battery": "Batterie", "charging": "Recharge", "power": "Puissance", "reservoir": "Réservoir", "colour": "Couleur standard", "magnif": "Grossissement", "image": "Image", "conn": "Connexion", "app": "Application", "light": "Lumière", "modes": "Modes", "water": "Résistance à l’eau", "runtime": "Autonomie", "heads": "Têtes", "type": "Type", "dispense": "Diffusion", "massage": "Massage", "mist": "Brume", "liquids": "Liquides", "motor": "Vitesse du moteur", "bristles": "Poils", "plate": "Plateau de brosse", "autooff": "Arrêt automatique", "dosing": "Chambre de dosage", "tips": "Embouts", "suction": "Aspiration", "base": "Socle", "vibration": "Vibration"},
    "de": {"material": "Material", "dims": "Abmessungen", "weight": "Nettogewicht", "battery": "Akku", "charging": "Laden", "power": "Leistung", "reservoir": "Reservoir", "colour": "Standardfarbe", "magnif": "Vergrößerung", "image": "Bild", "conn": "Verbindung", "app": "App", "light": "Licht", "modes": "Stufen", "water": "Wasserschutz", "runtime": "Laufzeit", "heads": "Aufsätze", "type": "Typ", "dispense": "Abgabe", "massage": "Massage", "mist": "Nebel", "liquids": "Flüssigkeiten", "motor": "Motordrehzahl", "bristles": "Borsten", "plate": "Bürstenplatte", "autooff": "Abschaltautomatik", "dosing": "Dosierkammer", "tips": "Spitzen", "suction": "Saugkraft", "base": "Standfuß", "vibration": "Vibration"},
    "es": {"material": "Materiales", "dims": "Dimensiones", "weight": "Peso neto", "battery": "Batería", "charging": "Carga", "power": "Potencia", "reservoir": "Depósito", "colour": "Color estándar", "magnif": "Aumento", "image": "Imagen", "conn": "Conexión", "app": "Aplicación", "light": "Luz", "modes": "Modos", "water": "Resistencia al agua", "runtime": "Autonomía", "heads": "Cabezales", "type": "Tipo", "dispense": "Dosificación", "massage": "Masaje", "mist": "Bruma", "liquids": "Líquidos", "motor": "Velocidad del motor", "bristles": "Cerdas", "plate": "Placa de cepillo", "autooff": "Apagado automático", "dosing": "Cámara dosificadora", "tips": "Puntas", "suction": "Succión", "base": "Base", "vibration": "Vibración"},
}


def _specs(lang, pairs):
    return [(LABELS[lang][k], v) for k, v in pairs]


# Each model: id, group ("scalp" or "face"), image list (path, w, h, key), and
# per-language copy. "suit" names the PAGES key for the "Suitable for" list.
MODELS = [
{
    "model": "KH-2306A", "group": "scalp", "suit": "suit_beauty",
    "files": [("assets/products/kh-2306a/kh-2306a-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Wireless scalp and hair camera",
            "card_p": "Handheld magnifying camera for viewing the scalp, hair and skin during a consultation. It streams to a phone over Wi-Fi.",
            "card_specs": ["50–200× magnification", "Wi-Fi to Android and iOS", "Rechargeable, USB-C"],
            "specs": [("magnif", "50–200×, manual focus"), ("image", "640 × 480, 30 fps"), ("conn", "Wi-Fi video stream to Android and iOS"), ("app", "Companion app; app and data-storage details available on request"), ("light", "Includes a blue-light viewing mode"), ("battery", "3.7 V, 400 mAh"), ("charging", "USB-C, 5 V"), ("power", "0.9 W"), ("dims", "29 × 35 × 124 mm"), ("weight", "55 g"), ("material", "ABS")],
            "steps": ["Charge the camera with the USB-C cable.", "Connect the phone to the camera over Wi-Fi and open the companion app.", "Place the lens on the scalp and turn the focus until the image is sharp.", "Take photos or videos to keep and compare at a later visit."],
            "note": "The camera switches off automatically after a set time. Clean the part that touches the skin as described in the instructions supplied with the product.",
            "alt": "KH-2306A wireless scalp and hair camera, white handheld body",
        },
        "zh": {
            "name": "无线头皮毛发放大相机",
            "card_p": "手持放大相机，咨询时用来查看头皮、毛发和皮肤，通过 Wi-Fi 把画面传到手机上。",
            "card_specs": ["50–200 倍放大", "Wi-Fi 连接安卓和 iOS", "USB-C 充电"],
            "specs": [("magnif", "50–200 倍，手动对焦"), ("image", "640 × 480，30 帧/秒"), ("conn", "Wi-Fi 视频流，支持安卓和 iOS"), ("app", "配套应用；应用和数据存储信息可按需提供"), ("light", "带蓝光查看模式"), ("battery", "3.7 V，400 mAh"), ("charging", "USB-C，5 V"), ("power", "0.9 W"), ("dims", "29 × 35 × 124 mm"), ("weight", "55 g"), ("material", "ABS")],
            "steps": ["用 USB-C 线给相机充电。", "手机通过 Wi-Fi 连接相机，打开配套应用。", "把镜头贴在头皮上，转动对焦直到画面清晰。", "拍照或录像保存，下次来访时对比。"],
            "note": "相机到设定时间会自动关机。接触皮肤的部分请按产品随附说明清洁。",
            "alt": "KH-2306A 无线头皮毛发放大相机，白色手持机身",
        },
        "fr": {
            "name": "Caméra sans fil pour cuir chevelu et cheveux",
            "card_p": "Caméra grossissante portative pour observer le cuir chevelu, les cheveux et la peau pendant une consultation. L’image est transmise au téléphone par Wi-Fi.",
            "card_specs": ["Grossissement 50–200×", "Wi-Fi vers Android et iOS", "Rechargeable, USB-C"],
            "specs": [("magnif", "50–200×, mise au point manuelle"), ("image", "640 × 480, 30 i/s"), ("conn", "Flux vidéo Wi-Fi vers Android et iOS"), ("app", "Application associée ; détails sur l’application et le stockage des données sur demande"), ("light", "Mode d’observation en lumière bleue"), ("battery", "3,7 V, 400 mAh"), ("charging", "USB-C, 5 V"), ("power", "0,9 W"), ("dims", "29 × 35 × 124 mm"), ("weight", "55 g"), ("material", "ABS")],
            "steps": ["Rechargez la caméra avec le câble USB-C.", "Connectez le téléphone à la caméra en Wi-Fi et ouvrez l’application associée.", "Posez l’objectif sur le cuir chevelu et réglez la mise au point jusqu’à obtenir une image nette.", "Prenez des photos ou des vidéos à conserver et à comparer lors d’une visite suivante."],
            "note": "La caméra s’éteint automatiquement après un temps défini. Nettoyez la partie en contact avec la peau selon les instructions fournies avec le produit.",
            "alt": "Caméra sans fil KH-2306A pour cuir chevelu et cheveux, boîtier portatif blanc",
        },
        "de": {
            "name": "Kabellose Kopfhaut- und Haarkamera",
            "card_p": "Handliche Vergrößerungskamera, um Kopfhaut, Haare und Haut bei einer Beratung anzusehen. Das Bild wird per WLAN auf ein Smartphone übertragen.",
            "card_specs": ["50- bis 200-fache Vergrößerung", "WLAN zu Android und iOS", "Akku, USB-C"],
            "specs": [("magnif", "50- bis 200-fach, manueller Fokus"), ("image", "640 × 480, 30 fps"), ("conn", "WLAN-Videostream zu Android und iOS"), ("app", "Begleit-App; Angaben zu App und Datenspeicherung auf Anfrage"), ("light", "Mit Blaulicht-Ansichtsmodus"), ("battery", "3,7 V, 400 mAh"), ("charging", "USB-C, 5 V"), ("power", "0,9 W"), ("dims", "29 × 35 × 124 mm"), ("weight", "55 g"), ("material", "ABS")],
            "steps": ["Die Kamera mit dem USB-C-Kabel laden.", "Das Smartphone per WLAN mit der Kamera verbinden und die Begleit-App öffnen.", "Die Linse auf die Kopfhaut setzen und den Fokus drehen, bis das Bild scharf ist.", "Fotos oder Videos aufnehmen, um sie beim nächsten Termin zu vergleichen."],
            "note": "Die Kamera schaltet sich nach einer festgelegten Zeit automatisch aus. Den Teil, der die Haut berührt, gemäß der mitgelieferten Anleitung reinigen.",
            "alt": "Kabellose Kopfhaut- und Haarkamera KH-2306A, weißes Handgerät",
        },
        "es": {
            "name": "Cámara inalámbrica para cuero cabelludo y cabello",
            "card_p": "Cámara de aumento portátil para observar el cuero cabelludo, el cabello y la piel durante una consulta. Transmite la imagen al teléfono por wifi.",
            "card_specs": ["Aumento de 50 a 200×", "Wifi a Android e iOS", "Recargable, USB-C"],
            "specs": [("magnif", "50–200×, enfoque manual"), ("image", "640 × 480, 30 fps"), ("conn", "Vídeo por wifi a Android e iOS"), ("app", "Aplicación complementaria; detalles de la aplicación y del almacenamiento de datos bajo petición"), ("light", "Incluye un modo de observación con luz azul"), ("battery", "3,7 V, 400 mAh"), ("charging", "USB-C, 5 V"), ("power", "0,9 W"), ("dims", "29 × 35 × 124 mm"), ("weight", "55 g"), ("material", "ABS")],
            "steps": ["Cargue la cámara con el cable USB-C.", "Conecte el teléfono a la cámara por wifi y abra la aplicación complementaria.", "Apoye la lente en el cuero cabelludo y gire el enfoque hasta que la imagen sea nítida.", "Tome fotos o vídeos para guardarlos y compararlos en una visita posterior."],
            "note": "La cámara se apaga automáticamente tras un tiempo programado. Limpie la parte que toca la piel según las instrucciones que acompañan al producto.",
            "alt": "Cámara inalámbrica KH-2306A para cuero cabelludo y cabello, cuerpo portátil blanco",
        },
    },
},
{
    "model": "KH-2401C", "group": "scalp", "suit": "suit_beauty",
    "files": [("assets/products/kh-2401c/kh-2401c-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Rechargeable serum-applicator comb",
            "card_p": "Cushioned comb with a refillable 4 ml reservoir. Roller balls release serum or hair oil between the teeth while the comb vibrates.",
            "card_specs": ["4 ml refillable reservoir", "Vibration massage", "Rechargeable, USB-C"],
            "specs": [("reservoir", "4 ml, separate and refillable"), ("dispense", "Roller balls between rounded teeth"), ("massage", "High-frequency vibration"), ("light", "Red LED, 655 nm"), ("battery", "150 mAh lithium"), ("charging", "USB-C, 5 V"), ("power", "Under 2 W"), ("dims", "220 × 70 × 38 mm"), ("weight", "105 g"), ("material", "ABS, silicone, nylon, metal"), ("colour", "Pink (other colours on request)")],
            "steps": ["Charge the comb with the USB-C cable.", "Fill the reservoir with serum or hair oil and close it.", "Switch on and comb slowly from the hairline towards the back of the head.", "Empty and rinse the reservoir after use."],
            "note": "The reservoir is separate from the comb body, which makes it easy to fill and clean.",
            "alt": "KH-2401C rechargeable serum-applicator comb in pink",
        },
        "zh": {
            "name": "充电式导液梳",
            "card_p": "气囊梳，带可加液的 4 ml 储液仓。梳齿间的滚珠出液，同时梳子微震按摩。",
            "card_specs": ["4 ml 可加液储液仓", "微震按摩", "USB-C 充电"],
            "specs": [("reservoir", "4 ml，独立可加液"), ("dispense", "圆润梳齿间滚珠出液"), ("massage", "高频微震"), ("light", "红色 LED，655 nm"), ("battery", "150 mAh 锂电池"), ("charging", "USB-C，5 V"), ("power", "低于 2 W"), ("dims", "220 × 70 × 38 mm"), ("weight", "105 g"), ("material", "ABS、硅胶、尼龙、金属"), ("colour", "粉色（其他颜色可定制）")],
            "steps": ["用 USB-C 线给梳子充电。", "在储液仓里加入精华或护发油，盖好。", "打开开关，从发际线向后脑慢慢梳。", "用完倒空储液仓并冲洗。"],
            "note": "储液仓与梳身分开，加液和清洗都方便。",
            "alt": "KH-2401C 充电式导液梳，粉色",
        },
        "fr": {
            "name": "Peigne applicateur de sérum rechargeable",
            "card_p": "Peigne à coussin d’air avec un réservoir rechargeable de 4 ml. Des billes libèrent le sérum ou l’huile capillaire entre les dents pendant que le peigne vibre.",
            "card_specs": ["Réservoir rechargeable de 4 ml", "Massage par vibration", "Rechargeable, USB-C"],
            "specs": [("reservoir", "4 ml, séparé et rechargeable"), ("dispense", "Billes entre des dents arrondies"), ("massage", "Vibration haute fréquence"), ("light", "LED rouge, 655 nm"), ("battery", "Lithium 150 mAh"), ("charging", "USB-C, 5 V"), ("power", "Moins de 2 W"), ("dims", "220 × 70 × 38 mm"), ("weight", "105 g"), ("material", "ABS, silicone, nylon, métal"), ("colour", "Rose (autres couleurs sur demande)")],
            "steps": ["Rechargez le peigne avec le câble USB-C.", "Remplissez le réservoir de sérum ou d’huile capillaire et refermez-le.", "Allumez le peigne et passez-le lentement de la lisière vers l’arrière de la tête.", "Videz et rincez le réservoir après usage."],
            "note": "Le réservoir est séparé du corps du peigne, ce qui facilite le remplissage et le nettoyage.",
            "alt": "Peigne applicateur de sérum rechargeable KH-2401C, rose",
        },
        "de": {
            "name": "Akku-Serumapplikator-Kamm",
            "card_p": "Kamm mit Luftkissen und nachfüllbarem 4-ml-Reservoir. Rollkugeln geben Serum oder Haaröl zwischen den Zinken ab, während der Kamm vibriert.",
            "card_specs": ["Nachfüllbares 4-ml-Reservoir", "Vibrationsmassage", "Akku, USB-C"],
            "specs": [("reservoir", "4 ml, separat und nachfüllbar"), ("dispense", "Rollkugeln zwischen abgerundeten Zinken"), ("massage", "Hochfrequente Vibration"), ("light", "Rote LED, 655 nm"), ("battery", "150-mAh-Lithium-Akku"), ("charging", "USB-C, 5 V"), ("power", "Unter 2 W"), ("dims", "220 × 70 × 38 mm"), ("weight", "105 g"), ("material", "ABS, Silikon, Nylon, Metall"), ("colour", "Rosa (andere Farben auf Anfrage)")],
            "steps": ["Den Kamm mit dem USB-C-Kabel laden.", "Das Reservoir mit Serum oder Haaröl füllen und schließen.", "Einschalten und langsam vom Haaransatz zum Hinterkopf kämmen.", "Das Reservoir nach der Anwendung leeren und ausspülen."],
            "note": "Das Reservoir ist vom Kammkörper getrennt und lässt sich daher leicht befüllen und reinigen.",
            "alt": "Akku-Serumapplikator-Kamm KH-2401C in Rosa",
        },
        "es": {
            "name": "Peine aplicador de sérum recargable",
            "card_p": "Peine con cojín de aire y depósito recargable de 4 ml. Unas bolas liberan el sérum o el aceite capilar entre las púas mientras el peine vibra.",
            "card_specs": ["Depósito recargable de 4 ml", "Masaje por vibración", "Recargable, USB-C"],
            "specs": [("reservoir", "4 ml, independiente y recargable"), ("dispense", "Bolas entre púas redondeadas"), ("massage", "Vibración de alta frecuencia"), ("light", "LED roja, 655 nm"), ("battery", "Litio de 150 mAh"), ("charging", "USB-C, 5 V"), ("power", "Menos de 2 W"), ("dims", "220 × 70 × 38 mm"), ("weight", "105 g"), ("material", "ABS, silicona, nailon, metal"), ("colour", "Rosa (otros colores bajo petición)")],
            "steps": ["Cargue el peine con el cable USB-C.", "Llene el depósito con sérum o aceite capilar y ciérrelo.", "Encienda el peine y péinese despacio desde la línea del cabello hacia la nuca.", "Vacíe y enjuague el depósito después del uso."],
            "note": "El depósito va separado del cuerpo del peine, por lo que es fácil de llenar y de limpiar.",
            "alt": "Peine aplicador de sérum recargable KH-2401C, rosa",
        },
    },
},
{
    "model": "KH-2408", "group": "scalp", "suit": "suit_beauty",
    "files": [("assets/products/kh-2408/kh-2408-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Hair-oil mist applicator",
            "card_p": "Handheld device that turns hair oil into a fine mist. The mist starts when the device senses the hair, and its strength can be adjusted.",
            "card_specs": ["8 ml chamber", "Adjustable, sensor-activated mist", "Rechargeable, USB-C"],
            "specs": [("reservoir", "8 ml"), ("mist", "Starts automatically, adjustable strength; no mesh plate"), ("liquids", "Designed for hair oils"), ("light", "Red, blue and mixed LED modes"), ("battery", "3.7 V, 900 mAh"), ("charging", "USB-C, 5 V"), ("water", "Waterproof body; rating available on request"), ("dims", "38 × 39.6 × 228 mm"), ("weight", "217 g"), ("material", "PCTG, ABS, metal"), ("colour", "Black (other colours on request)")],
            "steps": ["Charge the device with the USB-C cable.", "Fill the chamber with hair oil.", "Bring the teeth to the hair; the mist starts on its own.", "Set the mist strength and work section by section."],
            "note": "Clean the chamber after use, following the instructions supplied with the product.",
            "alt": "KH-2408 hair-oil mist applicator in black",
        },
        "zh": {
            "name": "发油喷雾仪",
            "card_p": "手持设备，把发油变成细雾。贴近头发会自动出雾，雾量可调。",
            "card_specs": ["8 ml 液仓", "感应出雾，雾量可调", "USB-C 充电"],
            "specs": [("reservoir", "8 ml"), ("mist", "感应自动出雾，雾量可调；非雾化片结构"), ("liquids", "适用于发油"), ("light", "红光、蓝光和红蓝混合 LED 模式"), ("battery", "3.7 V，900 mAh"), ("charging", "USB-C，5 V"), ("water", "整机防水；防水等级可按需提供"), ("dims", "38 × 39.6 × 228 mm"), ("weight", "217 g"), ("material", "PCTG、ABS、金属"), ("colour", "黑色（其他颜色可定制）")],
            "steps": ["用 USB-C 线充电。", "在液仓里加入发油。", "梳齿贴近头发，会自动出雾。", "调好雾量，分区操作。"],
            "note": "用完按产品随附说明清洁液仓。",
            "alt": "KH-2408 发油喷雾仪，黑色",
        },
        "fr": {
            "name": "Brumisateur d’huile capillaire",
            "card_p": "Appareil portatif qui transforme l’huile capillaire en brume fine. La brume démarre quand l’appareil détecte les cheveux, et son intensité se règle.",
            "card_specs": ["Chambre de 8 ml", "Brume réglable à détection", "Rechargeable, USB-C"],
            "specs": [("reservoir", "8 ml"), ("mist", "Démarrage automatique, intensité réglable ; sans plaque à mailles"), ("liquids", "Conçu pour les huiles capillaires"), ("light", "Modes LED rouge, bleu et mixte"), ("battery", "3,7 V, 900 mAh"), ("charging", "USB-C, 5 V"), ("water", "Corps étanche ; indice disponible sur demande"), ("dims", "38 × 39,6 × 228 mm"), ("weight", "217 g"), ("material", "PCTG, ABS, métal"), ("colour", "Noir (autres couleurs sur demande)")],
            "steps": ["Rechargez l’appareil avec le câble USB-C.", "Remplissez la chambre d’huile capillaire.", "Approchez les dents des cheveux ; la brume démarre seule.", "Réglez l’intensité et travaillez mèche par mèche."],
            "note": "Nettoyez la chambre après usage, selon les instructions fournies avec le produit.",
            "alt": "Brumisateur d’huile capillaire KH-2408, noir",
        },
        "de": {
            "name": "Haaröl-Nebelapplikator",
            "card_p": "Handgerät, das Haaröl in einen feinen Nebel verwandelt. Der Nebel startet, sobald das Gerät das Haar erkennt, und seine Stärke ist einstellbar.",
            "card_specs": ["8-ml-Kammer", "Einstellbarer Nebel mit Sensor", "Akku, USB-C"],
            "specs": [("reservoir", "8 ml"), ("mist", "Startet automatisch, Stärke einstellbar; ohne Vernebler-Plättchen"), ("liquids", "Für Haaröle ausgelegt"), ("light", "Rot-, Blau- und Mischlicht-LED-Modi"), ("battery", "3,7 V, 900 mAh"), ("charging", "USB-C, 5 V"), ("water", "Wasserdichtes Gehäuse; Schutzart auf Anfrage"), ("dims", "38 × 39,6 × 228 mm"), ("weight", "217 g"), ("material", "PCTG, ABS, Metall"), ("colour", "Schwarz (andere Farben auf Anfrage)")],
            "steps": ["Das Gerät mit dem USB-C-Kabel laden.", "Die Kammer mit Haaröl füllen.", "Die Zinken an das Haar führen; der Nebel startet von selbst.", "Die Nebelstärke einstellen und Partie für Partie arbeiten."],
            "note": "Die Kammer nach der Anwendung gemäß der mitgelieferten Anleitung reinigen.",
            "alt": "Haaröl-Nebelapplikator KH-2408 in Schwarz",
        },
        "es": {
            "name": "Aplicador de bruma de aceite capilar",
            "card_p": "Aparato portátil que convierte el aceite capilar en una bruma fina. La bruma se activa al detectar el cabello y su intensidad es regulable.",
            "card_specs": ["Cámara de 8 ml", "Bruma regulable con sensor", "Recargable, USB-C"],
            "specs": [("reservoir", "8 ml"), ("mist", "Se activa sola, intensidad regulable; sin placa de malla"), ("liquids", "Pensado para aceites capilares"), ("light", "Modos LED rojo, azul y mixto"), ("battery", "3,7 V, 900 mAh"), ("charging", "USB-C, 5 V"), ("water", "Cuerpo estanco; grado disponible bajo petición"), ("dims", "38 × 39,6 × 228 mm"), ("weight", "217 g"), ("material", "PCTG, ABS, metal"), ("colour", "Negro (otros colores bajo petición)")],
            "steps": ["Cargue el aparato con el cable USB-C.", "Llene la cámara con aceite capilar.", "Acerque las púas al cabello; la bruma se activa sola.", "Ajuste la intensidad y trabaje por secciones."],
            "note": "Limpie la cámara después del uso, según las instrucciones que acompañan al producto.",
            "alt": "Aplicador de bruma de aceite capilar KH-2408, negro",
        },
    },
},
{
    "model": "KH-2205", "group": "scalp", "suit": "suit_beauty",
    "files": [("assets/products/kh-2205/kh-2205-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Scalp-cleansing suction brush",
            "card_p": "Compact rechargeable brush. Its bristles loosen flakes and residue on the scalp, and gentle suction draws them in.",
            "card_specs": ["Two suction modes", "Magnetic, removable brush plate", "Rechargeable"],
            "specs": [("modes", "Two; airflow up to 3 m/s"), ("motor", "10,000 rpm"), ("bristles", "Boar bristle with round-tip nylon pins"), ("plate", "Magnetic, removable for cleaning"), ("autooff", "After 5 minutes"), ("battery", "3.7 V, 450 mAh"), ("charging", "5 V DC"), ("power", "2 W maximum"), ("dims", "75 × 76.5 × 55 mm"), ("weight", "80 g"), ("material", "ABS")],
            "steps": ["Charge the brush before first use.", "Choose one of the two modes.", "Move the brush slowly over the scalp, section by section.", "Detach the magnetic brush plate and clean it after use."],
            "note": "The brush switches off automatically after 5 minutes.",
            "alt": "KH-2205 scalp-cleansing suction brush, dark grey",
        },
        "zh": {
            "name": "头皮清洁吸屑梳",
            "card_p": "小巧的充电式清洁梳。刷毛把头皮上的皮屑和残留拨松，再用轻柔的吸力吸走。",
            "card_specs": ["两档吸力", "磁吸可拆齿盘", "充电式"],
            "specs": [("modes", "两档；最高风速 3 米/秒"), ("motor", "10000 转/分"), ("bristles", "猪鬃毛与尼龙圆头齿"), ("plate", "磁吸式，可拆下清洗"), ("autooff", "5 分钟后"), ("battery", "3.7 V，450 mAh"), ("charging", "5 V 直流"), ("power", "最大 2 W"), ("dims", "75 × 76.5 × 55 mm"), ("weight", "80 g"), ("material", "ABS")],
            "steps": ["首次使用前先充电。", "选择两档中的一档。", "分区在头皮上慢慢移动。", "用完取下磁吸齿盘清洗。"],
            "note": "5 分钟后会自动关机。",
            "alt": "KH-2205 头皮清洁吸屑梳，深灰色",
        },
        "fr": {
            "name": "Brosse d’aspiration nettoyante pour cuir chevelu",
            "card_p": "Brosse compacte et rechargeable. Ses poils décollent les squames et les résidus du cuir chevelu, puis une aspiration douce les recueille.",
            "card_specs": ["Deux modes d’aspiration", "Plateau magnétique amovible", "Rechargeable"],
            "specs": [("modes", "Deux ; flux d’air jusqu’à 3 m/s"), ("motor", "10 000 tr/min"), ("bristles", "Soies de sanglier et picots en nylon à bout rond"), ("plate", "Magnétique, amovible pour le nettoyage"), ("autooff", "Après 5 minutes"), ("battery", "3,7 V, 450 mAh"), ("charging", "5 V CC"), ("power", "2 W maximum"), ("dims", "75 × 76,5 × 55 mm"), ("weight", "80 g"), ("material", "ABS")],
            "steps": ["Rechargez la brosse avant la première utilisation.", "Choisissez l’un des deux modes.", "Passez lentement la brosse sur le cuir chevelu, zone par zone.", "Retirez le plateau magnétique et nettoyez-le après usage."],
            "note": "La brosse s’éteint automatiquement après 5 minutes.",
            "alt": "Brosse d’aspiration nettoyante KH-2205 pour cuir chevelu, gris foncé",
        },
        "de": {
            "name": "Kopfhaut-Reinigungsbürste mit Absaugung",
            "card_p": "Kompakte Akku-Bürste. Die Borsten lösen Schüppchen und Rückstände auf der Kopfhaut, eine sanfte Absaugung nimmt sie auf.",
            "card_specs": ["Zwei Saugstufen", "Magnetische, abnehmbare Bürstenplatte", "Akku"],
            "specs": [("modes", "Zwei; Luftstrom bis 3 m/s"), ("motor", "10.000 U/min"), ("bristles", "Wildschweinborsten mit Nylonstiften mit runder Spitze"), ("plate", "Magnetisch, zum Reinigen abnehmbar"), ("autooff", "Nach 5 Minuten"), ("battery", "3,7 V, 450 mAh"), ("charging", "5 V DC"), ("power", "Maximal 2 W"), ("dims", "75 × 76,5 × 55 mm"), ("weight", "80 g"), ("material", "ABS")],
            "steps": ["Die Bürste vor der ersten Anwendung laden.", "Eine der beiden Stufen wählen.", "Die Bürste langsam Partie für Partie über die Kopfhaut führen.", "Die magnetische Bürstenplatte abnehmen und nach der Anwendung reinigen."],
            "note": "Die Bürste schaltet sich nach 5 Minuten automatisch aus.",
            "alt": "Kopfhaut-Reinigungsbürste mit Absaugung KH-2205, dunkelgrau",
        },
        "es": {
            "name": "Cepillo limpiador de cuero cabelludo con succión",
            "card_p": "Cepillo compacto y recargable. Sus cerdas despegan las escamas y los residuos del cuero cabelludo, y una succión suave los recoge.",
            "card_specs": ["Dos modos de succión", "Placa magnética desmontable", "Recargable"],
            "specs": [("modes", "Dos; flujo de aire de hasta 3 m/s"), ("motor", "10 000 rpm"), ("bristles", "Cerdas de jabalí y púas de nailon de punta redonda"), ("plate", "Magnética, desmontable para limpiarla"), ("autooff", "A los 5 minutos"), ("battery", "3,7 V, 450 mAh"), ("charging", "5 V CC"), ("power", "2 W como máximo"), ("dims", "75 × 76,5 × 55 mm"), ("weight", "80 g"), ("material", "ABS")],
            "steps": ["Cargue el cepillo antes del primer uso.", "Elija uno de los dos modos.", "Pase el cepillo despacio por el cuero cabelludo, sección por sección.", "Retire la placa magnética y límpiela después del uso."],
            "note": "El cepillo se apaga automáticamente a los 5 minutos.",
            "alt": "Cepillo limpiador de cuero cabelludo con succión KH-2205, gris oscuro",
        },
    },
},
{
    "model": "KH-2403A", "group": "scalp", "suit": "suit_beauty",
    "files": [("assets/products/kh-2403a/kh-2403a-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Scalp applicator pen",
            "card_p": "Non-electric pen for applying serum along the hairline and the parting. It comes with a brush tip and a sponge tip.",
            "card_specs": ["17 ml reservoir", "Separate 1 ml dosing chamber", "Brush and sponge tips"],
            "specs": [("type", "Non-electric, no battery"), ("reservoir", "17 ml"), ("dosing", "1 ml, separate from the reservoir"), ("tips", "Brush tip and sponge tip"), ("dims", "Ø 20.5 × 118 mm"), ("weight", "28 g"), ("material", "PP; sponge or animal-hair brush tip")],
            "steps": ["Fill the reservoir with serum and close the pen.", "Choose the brush tip or the sponge tip.", "Apply along the hairline, the parting or other small areas.", "Close the cap for storage or travel."],
            "note": "A soft option for clients who prefer it to comb teeth. Clean the tip after use.",
            "alt": "KH-2403A scalp applicator pen with a clear reservoir",
        },
        "zh": {
            "name": "头皮涂液笔",
            "card_p": "不带电的涂液笔，用于沿发际线和发缝涂抹精华。配有毛刷头和海绵头。",
            "card_specs": ["17 ml 储液仓", "独立 1 ml 定量仓", "毛刷头和海绵头"],
            "specs": [("type", "不带电，无电池"), ("reservoir", "17 ml"), ("dosing", "1 ml，与储液仓分开"), ("tips", "毛刷头和海绵头"), ("dims", "Ø 20.5 × 118 mm"), ("weight", "28 g"), ("material", "PP；海绵或动物毛刷头")],
            "steps": ["在储液仓里加入精华，盖好笔身。", "选用毛刷头或海绵头。", "沿发际线、发缝或其他小范围涂抹。", "盖上笔帽，方便收纳或出行携带。"],
            "note": "适合不喜欢硬梳齿的客人。用完清洁涂抹头。",
            "alt": "KH-2403A 头皮涂液笔，透明储液仓",
        },
        "fr": {
            "name": "Stylo applicateur pour cuir chevelu",
            "card_p": "Stylo sans électronique pour appliquer un sérum le long de la lisière et de la raie. Il est fourni avec un embout pinceau et un embout éponge.",
            "card_specs": ["Réservoir de 17 ml", "Chambre de dosage séparée de 1 ml", "Embouts pinceau et éponge"],
            "specs": [("type", "Sans électronique, sans pile"), ("reservoir", "17 ml"), ("dosing", "1 ml, séparée du réservoir"), ("tips", "Embout pinceau et embout éponge"), ("dims", "Ø 20,5 × 118 mm"), ("weight", "28 g"), ("material", "PP ; embout éponge ou pinceau en poils d’animal")],
            "steps": ["Remplissez le réservoir de sérum et refermez le stylo.", "Choisissez l’embout pinceau ou l’embout éponge.", "Appliquez le long de la lisière, de la raie ou sur d’autres petites zones.", "Remettez le capuchon pour le rangement ou le voyage."],
            "note": "Une option douce pour les clients qui préfèrent éviter les dents de peigne. Nettoyez l’embout après usage.",
            "alt": "Stylo applicateur KH-2403A pour cuir chevelu avec réservoir transparent",
        },
        "de": {
            "name": "Kopfhaut-Applikatorstift",
            "card_p": "Stift ohne Elektronik zum Auftragen von Serum entlang des Haaransatzes und des Scheitels. Mit Pinselspitze und Schwammspitze.",
            "card_specs": ["17-ml-Reservoir", "Separate 1-ml-Dosierkammer", "Pinsel- und Schwammspitze"],
            "specs": [("type", "Ohne Elektronik, ohne Batterie"), ("reservoir", "17 ml"), ("dosing", "1 ml, vom Reservoir getrennt"), ("tips", "Pinselspitze und Schwammspitze"), ("dims", "Ø 20,5 × 118 mm"), ("weight", "28 g"), ("material", "PP; Schwamm- oder Tierhaarpinselspitze")],
            "steps": ["Das Reservoir mit Serum füllen und den Stift schließen.", "Pinselspitze oder Schwammspitze wählen.", "Entlang des Haaransatzes, des Scheitels oder auf anderen kleinen Bereichen auftragen.", "Die Kappe für Aufbewahrung oder Reise aufsetzen."],
            "note": "Eine sanfte Option für Kundinnen und Kunden, die keine Kammzinken mögen. Die Spitze nach der Anwendung reinigen.",
            "alt": "Kopfhaut-Applikatorstift KH-2403A mit transparentem Reservoir",
        },
        "es": {
            "name": "Lápiz aplicador para el cuero cabelludo",
            "card_p": "Lápiz sin electrónica para aplicar sérum a lo largo de la línea del cabello y la raya. Incluye una punta de pincel y una punta de esponja.",
            "card_specs": ["Depósito de 17 ml", "Cámara dosificadora de 1 ml aparte", "Puntas de pincel y de esponja"],
            "specs": [("type", "Sin electrónica, sin pilas"), ("reservoir", "17 ml"), ("dosing", "1 ml, separada del depósito"), ("tips", "Punta de pincel y punta de esponja"), ("dims", "Ø 20,5 × 118 mm"), ("weight", "28 g"), ("material", "PP; punta de esponja o pincel de pelo animal")],
            "steps": ["Llene el depósito con sérum y cierre el lápiz.", "Elija la punta de pincel o la de esponja.", "Aplique a lo largo de la línea del cabello, la raya u otras zonas pequeñas.", "Coloque el capuchón para guardarlo o para viajar."],
            "note": "Una opción suave para clientes que prefieren evitar las púas de un peine. Limpie la punta después del uso.",
            "alt": "Lápiz aplicador KH-2403A para el cuero cabelludo con depósito transparente",
        },
    },
},
{
    "model": "SR-2003B", "group": "face", "suit": "suit_face",
    "files": [("assets/products/sr-2003b/sr-2003b-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Pore suction device with magnifier",
            "card_p": "Suction device for facial pores with a built-in 2–5× magnifier, so the user can watch the area while working in front of a mirror.",
            "card_specs": ["2–5× acrylic magnifier", "Three silicone tips", "Adjustable suction"],
            "specs": [("magnif", "Acrylic magnifier, 2–5×"), ("tips", "Three silicone tips: large round, small round, oval"), ("suction", "Adjustable"), ("light", "Fill light for viewing"), ("base", "Anti-slip base"), ("battery", "3.7 V, 400 mAh"), ("charging", "5 V DC, about 2 h"), ("runtime", "1–2 h"), ("power", "Up to 2.5 W"), ("dims", "171 × 48 × 43.7 mm"), ("weight", "115 g"), ("material", "ABS, silicone"), ("colour", "White (other colours on request)")],
            "steps": ["Charge the device before first use.", "Fit the tip that suits the area.", "Start on the lowest suction level.", "Keep the tip moving while you watch through the magnifier. Do not hold it in one place."],
            "note": "Use in front of a mirror. Clean the silicone tips after use.",
            "alt": "SR-2003B pore suction device with magnifier, white",
        },
        "zh": {
            "name": "可视毛孔吸护仪",
            "card_p": "带 2–5 倍放大镜的面部毛孔吸护仪，对着镜子操作时能直接看到吸附部位。",
            "card_specs": ["2–5 倍亚克力放大镜", "三个硅胶吸头", "吸力可调"],
            "specs": [("magnif", "亚克力放大镜，2–5 倍"), ("tips", "三个硅胶吸头：大圆孔、小圆孔、椭圆孔"), ("suction", "可调"), ("light", "补光灯，便于观察"), ("base", "防滑底座"), ("battery", "3.7 V，400 mAh"), ("charging", "5 V 直流，约 2 小时"), ("runtime", "1–2 小时"), ("power", "最高 2.5 W"), ("dims", "171 × 48 × 43.7 mm"), ("weight", "115 g"), ("material", "ABS、硅胶"), ("colour", "白色（其他颜色可定制）")],
            "steps": ["首次使用前先充电。", "按部位装上合适的吸头。", "从最低档吸力开始。", "边通过放大镜观察边移动吸头，不要停在一处。"],
            "note": "对着镜子使用。用完清洁硅胶吸头。",
            "alt": "SR-2003B 可视毛孔吸护仪，白色",
        },
        "fr": {
            "name": "Appareil d’aspiration des pores avec loupe",
            "card_p": "Appareil d’aspiration pour les pores du visage avec une loupe intégrée 2–5×, pour voir la zone traitée en travaillant devant un miroir.",
            "card_specs": ["Loupe acrylique 2–5×", "Trois embouts en silicone", "Aspiration réglable"],
            "specs": [("magnif", "Loupe acrylique, 2–5×"), ("tips", "Trois embouts en silicone : grand rond, petit rond, ovale"), ("suction", "Réglable"), ("light", "Éclairage d’appoint pour mieux voir"), ("base", "Socle antidérapant"), ("battery", "3,7 V, 400 mAh"), ("charging", "5 V CC, environ 2 h"), ("runtime", "1 à 2 h"), ("power", "Jusqu’à 2,5 W"), ("dims", "171 × 48 × 43,7 mm"), ("weight", "115 g"), ("material", "ABS, silicone"), ("colour", "Blanc (autres couleurs sur demande)")],
            "steps": ["Rechargez l’appareil avant la première utilisation.", "Fixez l’embout adapté à la zone.", "Commencez au niveau d’aspiration le plus bas.", "Déplacez l’embout en continu en regardant à travers la loupe. Ne le maintenez pas au même endroit."],
            "note": "À utiliser devant un miroir. Nettoyez les embouts en silicone après usage.",
            "alt": "Appareil d’aspiration des pores SR-2003B avec loupe, blanc",
        },
        "de": {
            "name": "Porensauger mit Lupe",
            "card_p": "Sauggerät für Gesichtsporen mit eingebauter 2- bis 5-fach-Lupe, damit man den Bereich vor dem Spiegel im Blick behält.",
            "card_specs": ["Acryllupe 2- bis 5-fach", "Drei Silikonaufsätze", "Einstellbare Saugkraft"],
            "specs": [("magnif", "Acryllupe, 2- bis 5-fach"), ("tips", "Drei Silikonaufsätze: groß rund, klein rund, oval"), ("suction", "Einstellbar"), ("light", "Zusatzlicht zur besseren Sicht"), ("base", "Rutschfester Standfuß"), ("battery", "3,7 V, 400 mAh"), ("charging", "5 V DC, etwa 2 Std."), ("runtime", "1–2 Std."), ("power", "Bis 2,5 W"), ("dims", "171 × 48 × 43,7 mm"), ("weight", "115 g"), ("material", "ABS, Silikon"), ("colour", "Weiß (andere Farben auf Anfrage)")],
            "steps": ["Das Gerät vor der ersten Anwendung laden.", "Den passenden Aufsatz für den Bereich aufsetzen.", "Mit der niedrigsten Saugstufe beginnen.", "Den Aufsatz in Bewegung halten und dabei durch die Lupe schauen. Nicht an einer Stelle verweilen."],
            "note": "Vor einem Spiegel anwenden. Die Silikonaufsätze nach der Anwendung reinigen.",
            "alt": "Porensauger mit Lupe SR-2003B, weiß",
        },
        "es": {
            "name": "Aparato de succión de poros con lupa",
            "card_p": "Aparato de succión para los poros del rostro con lupa integrada de 2 a 5×, para ver la zona mientras se trabaja frente a un espejo.",
            "card_specs": ["Lupa acrílica de 2 a 5×", "Tres puntas de silicona", "Succión regulable"],
            "specs": [("magnif", "Lupa acrílica, 2–5×"), ("tips", "Tres puntas de silicona: redonda grande, redonda pequeña, ovalada"), ("suction", "Regulable"), ("light", "Luz auxiliar para ver mejor"), ("base", "Base antideslizante"), ("battery", "3,7 V, 400 mAh"), ("charging", "5 V CC, unas 2 h"), ("runtime", "1–2 h"), ("power", "Hasta 2,5 W"), ("dims", "171 × 48 × 43,7 mm"), ("weight", "115 g"), ("material", "ABS, silicona"), ("colour", "Blanco (otros colores bajo petición)")],
            "steps": ["Cargue el aparato antes del primer uso.", "Coloque la punta adecuada para la zona.", "Empiece con el nivel de succión más bajo.", "Mantenga la punta en movimiento mientras mira a través de la lupa. No la deje fija en un punto."],
            "note": "Úselo frente a un espejo. Limpie las puntas de silicona después del uso.",
            "alt": "Aparato de succión de poros SR-2003B con lupa, blanco",
        },
    },
},
{
    "model": "SR-1903", "group": "face", "suit": "suit_face",
    "files": [("assets/products/sr-1903/sr-1903-1.jpg", 800, 800, "main")],
    "copy": {
        "en": {
            "name": "Sonic facial cleansing brush",
            "card_p": "Compact cleansing brush with three sonic vibration levels and two heads. It charges wirelessly on its base.",
            "card_specs": ["Three vibration levels", "Bristle and silicone heads", "Wireless charging"],
            "specs": [("vibration", "Three levels: 60, 85 and 108 Hz"), ("heads", "Flat-bristle head and silicone head"), ("light", "Red LED"), ("battery", "3.7 V, 500 mAh"), ("charging", "Wireless, about 2 h"), ("runtime", "About 1.5 h"), ("power", "0.66 W"), ("water", "IPX6 (manufacturer specification)"), ("dims", "74 × 74 × 81 mm"), ("weight", "83 g"), ("material", "ABS"), ("colour", "White (other colours on request)")],
            "steps": ["Charge the brush on its base.", "Fit the bristle head or the silicone head.", "Wet the face and apply cleanser.", "Choose a level, move the head in small circles, then rinse the face."],
            "note": "Rinse the head after use and let it dry.",
            "alt": "SR-1903 sonic facial cleansing brush on its charging base, white",
        },
        "zh": {
            "name": "声波洁面刷",
            "card_p": "小巧的洁面刷，三档声波振动，配两种刷头，放在底座上无线充电。",
            "card_specs": ["三档振动", "平毛刷头和硅胶刷头", "无线充电"],
            "specs": [("vibration", "三档：60、85、108 Hz"), ("heads", "平毛刷头和硅胶刷头"), ("light", "红色 LED"), ("battery", "3.7 V，500 mAh"), ("charging", "无线充电，约 2 小时"), ("runtime", "约 1.5 小时"), ("power", "0.66 W"), ("water", "IPX6（厂家标称）"), ("dims", "74 × 74 × 81 mm"), ("weight", "83 g"), ("material", "ABS"), ("colour", "白色（其他颜色可定制）")],
            "steps": ["放在底座上充电。", "装上平毛刷头或硅胶刷头。", "打湿面部，涂上洁面产品。", "选好档位，小圈打圈移动，然后洗净面部。"],
            "note": "用完冲洗刷头并晾干。",
            "alt": "SR-1903 声波洁面刷放在充电底座上，白色",
        },
        "fr": {
            "name": "Brosse nettoyante sonique pour le visage",
            "card_p": "Brosse nettoyante compacte avec trois niveaux de vibration sonique et deux têtes. Elle se recharge sans fil sur son socle.",
            "card_specs": ["Trois niveaux de vibration", "Têtes à poils et en silicone", "Recharge sans fil"],
            "specs": [("vibration", "Trois niveaux : 60, 85 et 108 Hz"), ("heads", "Tête à poils plats et tête en silicone"), ("light", "LED rouge"), ("battery", "3,7 V, 500 mAh"), ("charging", "Sans fil, environ 2 h"), ("runtime", "Environ 1,5 h"), ("power", "0,66 W"), ("water", "IPX6 (spécification du fabricant)"), ("dims", "74 × 74 × 81 mm"), ("weight", "83 g"), ("material", "ABS"), ("colour", "Blanc (autres couleurs sur demande)")],
            "steps": ["Rechargez la brosse sur son socle.", "Fixez la tête à poils ou la tête en silicone.", "Mouillez le visage et appliquez le nettoyant.", "Choisissez un niveau, faites de petits cercles, puis rincez le visage."],
            "note": "Rincez la tête après usage et laissez-la sécher.",
            "alt": "Brosse nettoyante sonique SR-1903 sur son socle de recharge, blanche",
        },
        "de": {
            "name": "Schall-Gesichtsreinigungsbürste",
            "card_p": "Kompakte Reinigungsbürste mit drei Schallvibrationsstufen und zwei Aufsätzen. Sie lädt kabellos auf ihrem Standfuß.",
            "card_specs": ["Drei Vibrationsstufen", "Borsten- und Silikonaufsatz", "Kabelloses Laden"],
            "specs": [("vibration", "Drei Stufen: 60, 85 und 108 Hz"), ("heads", "Flachborstenaufsatz und Silikonaufsatz"), ("light", "Rote LED"), ("battery", "3,7 V, 500 mAh"), ("charging", "Kabellos, etwa 2 Std."), ("runtime", "Etwa 1,5 Std."), ("power", "0,66 W"), ("water", "IPX6 (Herstellerangabe)"), ("dims", "74 × 74 × 81 mm"), ("weight", "83 g"), ("material", "ABS"), ("colour", "Weiß (andere Farben auf Anfrage)")],
            "steps": ["Die Bürste auf dem Standfuß laden.", "Den Borsten- oder den Silikonaufsatz aufsetzen.", "Das Gesicht befeuchten und Reinigungsprodukt auftragen.", "Eine Stufe wählen, in kleinen Kreisen bewegen und das Gesicht danach abspülen."],
            "note": "Den Aufsatz nach der Anwendung abspülen und trocknen lassen.",
            "alt": "Schall-Gesichtsreinigungsbürste SR-1903 auf dem Ladestandfuß, weiß",
        },
        "es": {
            "name": "Cepillo sónico de limpieza facial",
            "card_p": "Cepillo de limpieza compacto con tres niveles de vibración sónica y dos cabezales. Se carga sin cables en su base.",
            "card_specs": ["Tres niveles de vibración", "Cabezal de cerdas y de silicona", "Carga inalámbrica"],
            "specs": [("vibration", "Tres niveles: 60, 85 y 108 Hz"), ("heads", "Cabezal de cerdas planas y cabezal de silicona"), ("light", "LED roja"), ("battery", "3,7 V, 500 mAh"), ("charging", "Inalámbrica, unas 2 h"), ("runtime", "Unas 1,5 h"), ("power", "0,66 W"), ("water", "IPX6 (especificación del fabricante)"), ("dims", "74 × 74 × 81 mm"), ("weight", "83 g"), ("material", "ABS"), ("colour", "Blanco (otros colores bajo petición)")],
            "steps": ["Cargue el cepillo en su base.", "Coloque el cabezal de cerdas o el de silicona.", "Moje el rostro y aplique el limpiador.", "Elija un nivel, haga pequeños círculos y después aclare el rostro."],
            "note": "Enjuague el cabezal después del uso y déjelo secar.",
            "alt": "Cepillo sónico de limpieza facial SR-1903 en su base de carga, blanco",
        },
    },
},
]

for _m in MODELS:
    for _lang, _c in _m["copy"].items():
        _c["specs"] = _specs(_lang, _c["specs"])


def by_group(group):
    return [m for m in MODELS if m["group"] == group]

DESC_SUFFIX = {
    "en": "Request a quote or a sample from AuraBridge.",
    "zh": "可向 AuraBridge 索取报价或样品。",
    "fr": "Demandez un devis ou un échantillon à AuraBridge.",
    "de": "Angebot oder Muster bei AuraBridge anfordern.",
    "es": "Solicite un presupuesto o una muestra a AuraBridge.",
}
