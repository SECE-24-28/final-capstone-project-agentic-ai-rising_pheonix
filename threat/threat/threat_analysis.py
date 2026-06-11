# -*- coding: utf-8 -*-
    urgency = detect_urgency(message)

    scam_keywords = detect_scam_keywords(message)

    llm_result = llm_analysis(message)

    risk_score = 0

    if links["found"]:
        risk_score += 30

    risk_score += len(urgency) * 10

    risk_score += len(scam_keywords) * 10

    risk_score = min(risk_score, 100)

    if risk_score > 70:
        risk_level = "HIGH"

    elif risk_score > 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "links_detected": links["links"],
        "urgency_words": urgency,
        "suspicious_keywords": scam_keywords,
        "llm_explanation": llm_result
    }

sample_message = """
Congratulations!

You have won a $500 Amazon Gift Card.

Claim your reward immediately.

Click here:
https://fake-reward.com

Offer expires today.
"""

result = threat_analysis_agent(sample_message)
