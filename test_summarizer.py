from summarizer import summarize_text

sample_text = """
Today we discussed the AI project.
Tejesh will prepare the backend API by Friday.
Frontend work will start next week.
"""

summary = summarize_text(sample_text)

print("SUMMARY OUTPUT:")
print(summary)
