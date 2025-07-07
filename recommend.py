
from translate_text import translate

def get_recommendations(age, cholesterol, bp, exercise, lang='en'):
    suggestions = []
    if cholesterol > 200:
        suggestions.append(translate("⚠️ Reduce high-cholesterol foods like red meat and fried food.", lang))
    if bp > 130:
        suggestions.append(translate("⚠️ Monitor your blood pressure and reduce salt intake.", lang))
    if exercise == translate("No", lang):
        suggestions.append(translate("✅ Start 30 min of daily walking or yoga.", lang))
    if age > 50:
        suggestions.append(translate("🔁 Get annual checkups and ECG tests.", lang))
    if not suggestions:
        suggestions.append(translate("✅ You're doing great! Keep up a heart-healthy lifestyle.", lang))
    return suggestions
