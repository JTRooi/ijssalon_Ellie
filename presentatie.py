def presenteer(mijn_dict, bedrag):
    
    for smaak, bedrag in mijn_dict.items():
        print(f"{smaak}: {bedrag} euro")
        bedrag = sum(mijn_dict.values())
        
    print("==========================")

    print(f"Totaal : {bedrag} euro")