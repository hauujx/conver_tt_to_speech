import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'}
    try:
        response = requests.get(url,headers=header)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text_data = soup.get_text()
        text_data = soup.find_all('div','chapter-c')
        tilename = str(soup.find_all('div','chapter-title'))
        tilename = tilename.replace(tilename[-7:],'')
        tilename = tilename.replace('\n','')
        text_data = str(text_data) 
        lenght = len(text_data) - 140
        text_data=text_data.replace(r"<br/><br/>",' ')
        text_data=text_data.replace("”“",' ')
        
        text_data=text_data.replace("”",' ')
        text_data=text_data[31:lenght]+'.Hết chương '
        return text_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def split_text_into_chunks(text, chunk_size=500):
    
    chunks = []
    current_chunk = ""

    for char in text:
        if len(current_chunk) < chunk_size:
            current_chunk += char
        elif char.isspace():
            chunks.append(current_chunk)
            current_chunk = char
        else:
            # Lùi lại 1 ký tự cho đến khi gặp dấu cách
            while current_chunk and not current_chunk[-1].isspace():
                char = current_chunk[-1] + char
                current_chunk = current_chunk[:-1]

            chunks.append(current_chunk)
            current_chunk = char

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
 
    if current_chunk:
        chunks.append(current_chunk)

    return chunks

if __name__ == "__main__":
    url = "https://truyenfull.vn/kiem-phap-vuong-gia/chuong-670/"  # Thay đổi URL này bằng đường dẫn thực tế
    data = get_text_from_url(url)

    if data:
        list_ss = split_text_into_chunks(data)
        for i, chunk in enumerate(list_ss):
            print(f"Chunk {i + 1}:", chunk)