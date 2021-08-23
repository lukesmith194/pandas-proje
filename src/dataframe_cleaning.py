import re




def clear_whitspaces_columns(df):
    """
    Clears whitespaces from the columns in a dataframe 
    """
    
    print(type(df))
    col = df.columns
    
    col= [i.strip() for i in col]
    col=[i.replace(" ", "") for i in col]


    df.columns = col
    

def limpiar(x):
    """
    Cleans out activity column and joins similar activities into the same 
    group.
    input:
        string
    returns:
        correct string with activities grouped up
    
    """
    surfing = re.findall(r"[S|s]urf\w+|[B|b]ody\w+",str(x))
    fishing = re.findall(r"[F|f]ish\w+|[W|w]ade\w+|[W|w]ork\w+|[C|c]ollect\w+",str(x))
    swimming = re.findall(r"[S|s]wim\w+|[B|b]ath\w+|[F|f]loat\w+",str(x))
    diving = re.findall(r"[D|d]ivi\w+",str(x))
    standing = re.findall(r"[W|w]alk\w+|[F|f]ell\w+|[S|s]tand\w+|[S|s]too\w+", str(x))
    boating = re.findall(r"[S|s]hip\w+|[S|s]ail\w+|[F|f]erry\w+|[K|k]ayak\w+|[W|w]ake\w+",str(x))
    
    if diving:
        return "diving"
    elif surfing:
        return "surfing"
    elif fishing:
        return "fishing"
    elif swimming:
        return "swimming"
    elif diving:
        return "diving"
    elif standing:
        return "standing"
    elif boating:
        return "boating"
    else:
        return "unknown"

def clean_species(x):
    """
        Cleans out species column and joins similar activities into the same 
    group.
    input:
        string
    returns:
        correct string with activities grouped up
    """
    reef= re.findall(r"[R|r]ee\w+",str(x))
    white= re.findall(r"[W|w]hit\w+",str(x))
    wobbegong= re.findall(r"[W|w]obbegon\w+",str(x))
    tawney= re.findall(r"[T|t]awne\w+",str(x))
    blacktip= re.findall(r"[B|b]lackti\w+",str(x))
    bull= re.findall(r"[B|b]ul\w+",str(x))
    tiger= re.findall(r"[T|t]ige\w+",str(x))
    bronze_whale= re.findall(r"[B|b]ronz\w+",str(x))
    mako= re.findall(r"[M|m]ak\w+",str(x))
    grey_nurse= re.findall(r"[G|g]re\w+",str(x))
    
    if reef:
        return "reef"
    elif white:
        return "white"
    elif wobbegong:
        return "wobbegong"
    elif tawney:
        return "tawney"
    elif blacktip:
        return "blacktip"
    elif bull:
        return "bull"
    elif tiger:
        return "tiger"
    elif bronze_whale:
        return "bronze whale"
    elif mako:
        return "mako"
    elif grey_nurse:
        return "grey nurse"
    else:
        return "other"