import sys
from workflow import Workflow, ICON_WEB, web

def main(wf):
    base_url = "http://kitapmetre.com"

    if len(wf.args):
        query = wf.args[0]
        query = query.replace(" ", "%20")
    else:
        query = None

    url = 'http://kitapmetre.com/a/ac?term='+query
    r = web.get(url)
    r.raise_for_status()
    result = r.json()

    kitaplar = result

    for kitap in kitaplar:
        wf.add_item(title=kitap['t'], arg=base_url+kitap['u'], valid=True)
    
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))