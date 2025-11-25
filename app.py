import gradio as gr
from datetime import datetime

# ---------------------------------------------------------------------------
# Backend placeholder logic
# ---------------------------------------------------------------------------

def process_message(message, files, history):
    """Simple placeholder logic — replace with your threat-intel engine."""
    response = f"Received: {message}"
    if files:
        response += f" | Files: {[f.name for f in files]}"
    history = history + [(message, response)]
    return history, history

def clear_chat():
    return [], []

def download_chat(history):
    """Convert chat history to a downloadable text string."""
    output = ""
    for user_msg, bot_msg in history:
        output += f"[User]: {user_msg}\n[System]: {bot_msg}\n\n"
    return output

# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

with gr.Blocks(title="Threat-Intel Chat Interface") as demo:

    gr.Markdown("### 🛰 Intelligence Chat Console")

    # Chat history is stored in a gr.State object
    chat_state = gr.State([])

    with gr.Row():
        chat = gr.Chatbot(height=450, label="Dialogue Stream")
        with gr.Column(scale=0.4):
            file_input = gr.File(label="Upload Files", file_count="multiple")
            clear_btn = gr.Button("Clear Chat", variant="secondary")
            download_btn = gr.Button("Download Transcript")

    with gr.Row():
        user_input = gr.Textbox(
            placeholder="Type your message...",
            label="User Input"
        )
        send_btn = gr.Button("Send", variant="primary")

    # Event wiring
    send_btn.click(
        fn=process_message,
        inputs=[user_input, file_input, chat_state],
        outputs=[chat, chat_state]
    )

    user_input.submit(
        fn=process_message,
        inputs=[user_input, file_input, chat_state],
        outputs=[chat, chat_state]
    )

    clear_btn.click(
        fn=clear_chat,
        inputs=None,
        outputs=[chat, chat_state]
    )

    download_btn.click(
        fn=download_chat,
        inputs=chat_state,
        outputs=gr.File()
    )

demo.launch()