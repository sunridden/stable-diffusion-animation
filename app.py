import gradio as gr
import replicate

def showAnimation(startingPrompt, endingPrompt):
    model = replicate.models.get("andreasjansson/stable-diffusion-animation")
    version = model.versions.get("ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5")
    output = version.predict(prompt_start=startingPrompt, prompt_end=endingPrompt)
    return output

# START OF PAGE
demo = gr.Interface(
        fn=showAnimation, 
        inputs=["text", "text"], 
        outputs="image",
        title = "Stable Diffusion Animation",
        description = "Text-to-animation",
        allow_flagging="never"
)

demo.launch(share=True)
  
