import sys
import requests


def download_url_and_get_all_hrefs(url):
    hrefs = []

    response = requests.get(url)  #stáhne stránku a uloží do responce

    if response.status_code != 200:     #ověří že se podařilo stránku stáhnou
        raise Exception("Stranku se nepodarilo stahnout.")

    html = response.text    #převede html na běžný text

    while '<a href="' in html:
        start = html.find('<a href="') + len('<a href="')   #find najde pozici na které začíná hledaný text
        end = html.find('"', start)
        #find uloží do proměné end -1 pokud nenajde hledaný znak

        if end == -1:   #kontrola zda v proměné end není náhodou -1
            break

        odkaz = html[start:end]   #do proměné "odkaz" vyseknu z html textu to co je mezi pozicí start a end tj (hledaný odkaz)
        hrefs.append(odkaz)

        html = html[end + 1:]  #do html uloží celý zbývající text od end +1 až do konce tj (vynechá již prohledanou část)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        seznam = download_url_and_get_all_hrefs(url)

        for odkaz in seznam:
            print(odkaz)

    except IndexError:
        print("Zadejte URL adresu stranky.")

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
