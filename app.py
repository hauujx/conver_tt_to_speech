from flask import Flask, render_template, request,url_for,send_file
import os
import crawl_ok
import crawl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    data = crawl_ok.get_text_from_url(url)
    list_ss =crawl_ok.split_text_into_chunks(data)
    crawl.conver_mp3(list_ss)
    
    if data:
        list_ss = crawl_ok.split_text_into_chunks(data)
        
        return render_template('result.html', list_ss=list_ss )
    else:
        return render_template('error.html')
@app.route('/download')
def download():
    file_paths = f'test3.mp3'
    file_paths = os.path.join(os.path.dirname(__file__), file_paths)
    
    return send_file(file_paths,as_attachment=True)



if __name__ == '__main__':
     app.run(debug=True)

