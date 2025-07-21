
from openai.types.responses import ResponseTextDeltaEvent

async def stream_response(result_stream, user_context):
    assistant_reply = ""

    async for event in result_stream.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            delta = event.data.delta
            print(delta, end="", flush=True)
            assistant_reply += delta

    user_context.messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply