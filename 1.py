import asyncio
import edge_tts  

TEXT = "你好啊，我是杭州电子科技大学的虚拟数字人，有什么可以帮忙的？"
VOICE = "zh-CN-XiaoyiNeural"  
OUTPUT_FILE = "F:/EDGE-TTS/test.mp3"

async def _main() -> None:  
    communicate = edge_tts.Communicate(TEXT, VOICE)  
    await communicate.save(OUTPUT_FILE)  

if __name__ == "__main__":  
    asyncio.run(_main())