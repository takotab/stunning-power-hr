import utils
import html


def div(text):
    return "<div>" + text + "</div>"


def h1(text):
    return "<h1>" + text + "</h1>"


def h2(text):
    return "<h2>" + text + "</h2>"


newline = h2(" ")


def make_html(file):
    result = h1("Max test " + utils.get_date(file) + "  " + utils.get_name(file))
    img = list(utils.get_file(name=utils.get_name(file), filetype=".jpg"))
    if img:
        result += (
            '<img src="/home/tako/google_drive/Projecten/sport/stunning-power-hr/'
            + img[0]
            + '" style="width:==438px;height:438px;">'
        )
    result += (
        '<img src="/home/tako/google_drive/Projecten/sport/stunning-power-hr/'
        + file.replace(".fit", "_plot.png")
        + '">'
    )
    t = html.Table(header_row=["Item", "Waarde (30 seconden)"])
    for key, item in utils.get_info(file).items():
        if key in ["Max hartslag (bpm)", "Max power (W)", "Max power per kg (W/kg)"]:
            t.rows.append([html.TableCell(key), html.TableCell(str(item))])
    if utils.get_info(file)['sex'] == 'm':
        t.rows.append([html.TableCell("Max power per kg (W/kg) geschat Chris Froome"), html.TableCell(str(8.3))])
    if utils.get_info(file)['sex'] == 'w':
        t.rows.append([html.TableCell("Max power per kg (W/kg) geschat Anna van der Breggen"), html.TableCell(str(7.2))])
        
    result += (
        str(t)
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
        + newline
        + h2(" ")
        + newline
    )
    result += newline + h2("Trainings advies") + newline
    t = html.Table(header_row=["Zone", "start", "eind"])

    for key, item in utils.get_info(file)["hr-zones"].items():
        t.rows.append(
            [
                html.TableCell(key),
                html.TableCell(str(item[0])),
                html.TableCell(str(item[1])),
            ]
        )
    result += str(t)
    result += (
        newline
        + newline
        + h2(" ")
        + newline
        + "Grofweg bestaan er twee trainingsmodellen, het zogenaamde drempel model (in het Engels:"
        + "threshold) en het gepolariseerde model (in het Engels: polarized). Het gepolariseerde trainingsmodel "
        + "is momenteel aanbevolen. In dit model wordt er geen aandacht meer besteed aan training op of rond "
        + "de 1e ventilatoire drempel (in D3). Dit model gaat ervan uit dat 80% van je training uit laag intensieve "
        + "inspanning bestaat (onder D3) en de overige 20% "
        + "uit zeer intensieve inspanning (boven D3). Het idee hierachter is dat je "
        + "tijdens een wedstrijd ook een intensiteit bereikt die ruim boven je drempel ligt, waardoor training op "
        + "je 1e drempel minder effect heeft. Hiernaast wordt dan nog kracht training gedaan."
        + newline
        + "Voor meer informatie in het nederlands: https://www.allesoversport.nl/artikel/polarized-training-voor-duursporters/"
        + newline
        + "In het engels: http://tradewindsports.net/training/polarized-training-rip-threshold-training/"
        + newline
        + "Voor nerds: https://elementssystem.com/wp-content/uploads/2018/05/Hydren.pdf"
    )
    return result
