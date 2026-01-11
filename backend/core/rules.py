# backend/core/rules.py

def calculate_risk_score(metadata, typo_target):
    """
    Decides the risk level based on:
    1. Does it exist? (metadata)
    2. Is it a typo? (typo_target)
    """
    
    # 1. IF PACKAGE EXISTS -> SAFE
    # If we found metadata, the package is real.
    if metadata:
        return {
            "level": "SAFE",
            "score": 0,
            "color": "green",
            "status": "Verified",
            "reasons": ["Package exists on official registry."]
        }

    # 2. IF PACKAGE DOES NOT EXIST... CHECK FOR TYPO (The Innovation Layer)
    # It's missing, but it looks like a popular package? -> Suggestion
    if typo_target:
        return {
            "level": "HIGH",
            "score": 90,
            "color": "orange",
            "status": "Typosquatting Detected",
            "suggestion": f"Did you mean '{typo_target}'? (Confidence: High)",
            "reasons": [
                f"The package '{typo_target}' is very popular.",
                "This input looks like a typo-squatting attack or mistake."
            ]
        }

    # 3. IF MISSING AND NO TYPO -> HALLUCINATION
    return {
        "level": "CRITICAL",
        "score": 100,
        "color": "red",
        "status": "AI Hallucination",
        "reasons": ["Package not found. This name is available for hackers to register malware."]
    }