#!/usr/bin/env python3
#
# Transposition Cipher Hacker

from columnar_transposition_cipher import decrypt
from detect_english import is_english


def hack_transposition(msg):
    """Hack transposition cipher.

    :param msg: the input message
    :type msg: str

    :return: decrypted message or None
    """

    print("Hacking...")
    print("(Press Ctrl-C to quit at any time.)")

    for key in range(1, len(msg)):
        print("Trying key #{}...".format(key))
        decrypted_text = decrypt(key, msg)
        if is_english(decrypted_text):
            print()
            print("Possible encryption hack:")
            print("Key {}: {}".format(key, decrypted_text[:100]))
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input("> ")
            if response.strip().upper().startswith("D"):
                return decrypted_text
    return None


def main():
    """Main program."""

    msg = """Iai"t-ovirdan  nennmhn upenrnshtnesoa gsmet teeebra  eepma,  mrr aattw dnsr nptn rsr mt detikieeti ,aayrh ae nsaiYsqodezr hav nd oeWdacihdmo.u   a fatindvsb avdaseeeu"etistcitedosealple nh   T\nshtiion let.rieokrf isswu\nte gonddyo  tdmsetaunaoebY  hnnt o saBi.strispgim eofCai rter lus\n ,,std deh uoNdfoohsemlte\nk  ieae  auTrN inlanme  rIeCtnrtxtsvnu  "c st\'oevwsteiag ephtetbcipaY  tvtie spsl,t,ear ieonanoaa e d a  ck h rtipl mvrtundc oeanshoesali du dmet Tdsotuordta\'dunee"eltiesncu  mhrse aps c anwslhdntehbgmpo   gtp ahtdch eentiraerilsawceeecb hieitd \'.gen esyediotmnhoaen.lo pt\nadgwat  vlmteiius g"e al \nt eitawaelminnet m \n claiIiwstekidr intgf wet\nGoltmnoi hretstbtg   thdoIom fm ntt  nh.iet domhei nobooea hostl  s etinaenaw ganrd l  tryoWeadhd r   htltlmisaohra uerp inikcspahe i atsuoinrr  pts\'tehelte tnhtatrwcsa kfro tstana  aheaet   tpnpnro r  ilstcone slemawea ooipwiapnlifard a ymoderralwerogdlgetoni idm env  egi nirhda nir gFsvernteapnactdaktrtogvmbiasetethrpociihlti,effeesencur s ,tplyneayen"sofs \' aeetopr iri.sst  g sri i alb,iuoeYsoc"t, gf t mcosa  o srnsoeai\n  euowhw.efslbvoai dpurce\ncwviriehr ugrektns oTshs"oeed t y,oeoar  gttnu  ,Wn neahc  nsrnsht aodbtm hti ll otKl idiahfn ieoobeemwilomh"""
    hacked_msg = hack_transposition(msg)
    if hacked_msg is None:
        print("Failed to hack encryption.")
    else:
        print("\nCopying decrypted text to screen:\n")
        print(hacked_msg)


if __name__ == "__main__":
    main()

