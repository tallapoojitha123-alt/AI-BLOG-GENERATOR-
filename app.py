!pip -q install google-genai gradio
import gradio as gr
from google import genai

# Initialize the Gemini client
client = genai.Client(api_key="")

def generate_blog(topic, audience, tone, words, keywords):
    # Construct the enhanced prompt with SEO instructions
    prompt = f"""
    Write a {words}-word blog post.

    Topic: {topic}
    Audience: {audience}
    Tone: {tone}
    Target Keywords to include: {keywords}

    Structure requirements:
    - Catchy Title
    - Introduction
    - Key Points (with subheadings)
    - Practical Examples
    - Conclusion

    SEO Requirement: Seamlessly integrate the target keywords. Bold them in the output text so I can see where they were used.
    """

    # Fixed the typo from 'conents' to 'contents'
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# Build the Gradio Interface
demo = gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic", placeholder="e.g., Remote Work Productivity"),
        gr.Textbox(label="Audience", placeholder="e.g., Freelancers and Tech Managers"),
        gr.Dropdown(
            ["Professional", "Casual", "Formal", "Funny", "Inspirational"],
            label="Tone",
            value="Casual"
        ),
        gr.Slider(200, 1000, step=500, value=500, label="Word Count"),
        # New SEO Feature Input
        gr.Textbox(label="SEO Keywords (Comma separated)", placeholder="e.g., time management, remote tools, deep work")
    ],
    outputs="markdown",
    title="AI Blog Generator with SEO Optimizer (Gemini)",
    description="Generate structured, audience-targeted blog posts with optimized SEO keywords."
)

if _name_ == "_main_":
    demo.launch()
