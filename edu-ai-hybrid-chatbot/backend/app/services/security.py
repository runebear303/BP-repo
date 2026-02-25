def sanitize_prompt(text: str):
    blacklist = [
        "system:", "ignore instructions", "jailbreak",
        "developer mode", "role:", "act as",
        "negeer instructies", "omzeil", "doe alsof"
    ]

    for b in blacklist:
        text = text.replace(b, "")

    # Token / length limit (security)
    return text[:500]
    
