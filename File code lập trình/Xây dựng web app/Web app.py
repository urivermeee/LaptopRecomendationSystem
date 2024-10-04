from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Định nghĩa Flask app
app = Flask(__name__)

folder_path = 'C:\\Users\\TECHCARE\\Desktop\\crawl_project\\web'
product_info = 'cleaned_product_info.xlsx'
fpt_price = 'cleaned_fpt_price.xlsx'
thegioididong_price = 'cleaned_thegioididong_price.xlsx'
cellphones_price = 'cleaned_cellphones_price.xlsx'
hacom_price = 'cleaned_hacom_price.xlsx'
nguyenkim_price = 'cleaned_nguyenkim_price.xlsx'
hangchinhhieu_price = 'cleaned_hangchinhhieu_price.xlsx'
phongvu_price = 'cleaned_phongvu_price.xlsx'
gearvn_price = 'cleaned_gearvn_price.xlsx'

# Đọc file Excel
df = pd.read_excel(f'{folder_path}/{product_info}')
fpt = pd.read_excel(f'{folder_path}/{fpt_price}')
tgd = pd.read_excel(f'{folder_path}/{thegioididong_price}')
cps = pd.read_excel(f'{folder_path}/{cellphones_price}')
hac = pd.read_excel(f'{folder_path}/{hacom_price}')
nk = pd.read_excel(f'{folder_path}/{nguyenkim_price}')
hch = pd.read_excel(f'{folder_path}/{hangchinhhieu_price}')
pv = pd.read_excel(f'{folder_path}/{phongvu_price}')
gvn = pd.read_excel(f'{folder_path}/{gearvn_price}')

dt = df.copy()
dt['features'] = dt['categorize_laptop'] + ' '  + dt['price_bin']  + ' ' + dt['product_brand']  + ' ' + dt['product_size_bin'] + ' ' + dt['product_color'] + ' ' + dt['product_weight'] + ' ' + dt['product_material_type'] + ' ' + dt['CPU_filter'] + ' '+ dt['RAM_capacity'] + ' ' + dt['hard_driver'] 
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(dt['features'])

# Route chính của ứng dụng
@app.route('/')
def index():
    return render_template('recommendation_form.html')

# Route để xử lý yêu cầu đề xuất laptop
@app.route('/laptop_recommender', methods=['POST'])
def laptop_recommender():
    propose = request.form['propose']
    price = request.form['price']
    brand = request.form['brand']
    size = request.form['size']
    color = request.form['color']
    weight = str(request.form['weight']) + ' kg'
    material = request.form['material']
    cpu = request.form['cpu']
    ram = request.form['ram']
    hard_driver = request.form['hard_driver']

    # Hàm để đề xuất laptop dựa trên thông tin từ form
    def get_laptop_recommendations(propose, price, brand, size, color, weight, material, cpu, ram, hard_driver, dt=dt):
        input_info = f"Nhu cầu sử dụng: {propose} - Giá: {price} - Hãng: {brand} - Kích cỡ: {size} - Màu sắc: {color} - Trọng lượng: {weight} - Chất liệu: {material} - Loại CPU: {cpu} - Dung tích RAM: {ram} - Lưu trữ: {hard_driver}"
        input_features = f"{propose} {price} {brand} {size} {color} {weight} {material} {cpu} {ram} {hard_driver}"
        input_tfidf = tfidf.transform([input_features])
        cosine_similarities = linear_kernel(input_tfidf, tfidf_matrix).flatten()
        sim_scores = sorted(enumerate(cosine_similarities), key=lambda x: x[1], reverse=True)[:12]
        laptop_indices = [i[0] for i in sim_scores]
        recommended_laptops = dt.iloc[laptop_indices]
        recommended_laptops_id = dt['product_id'].iloc[laptop_indices]
        fpt_recommended_laptop = fpt[fpt['product_id'].isin(recommended_laptops_id)]
        tgd_recommended_laptop = tgd[tgd['product_id'].isin(recommended_laptops_id)]
        cps_recommended_laptop = cps[cps['product_id'].isin(recommended_laptops_id)]
        gvn_recommended_laptop = gvn[gvn['product_id'].isin(recommended_laptops_id)]
        pv_recommended_laptop = pv[pv['product_id'].isin(recommended_laptops_id)]
        nk_recommended_laptop = nk[nk['product_id'].isin(recommended_laptops_id)]
        hac_recommended_laptop = hac[hac['product_id'].isin(recommended_laptops_id)]
        hch_recommended_laptop = hch[hch['product_id'].isin(recommended_laptops_id)]
        web_recommended_laptops_info = [
            fpt_recommended_laptop.to_dict(orient='records'),
            tgd_recommended_laptop.to_dict(orient='records'),
            cps_recommended_laptop.to_dict(orient='records'),
            gvn_recommended_laptop.to_dict(orient='records'),
            pv_recommended_laptop.to_dict(orient='records'),
            nk_recommended_laptop.to_dict(orient='records'),
            hac_recommended_laptop.to_dict(orient='records'),
            hch_recommended_laptop.to_dict(orient='records')
        ]
        recommended_laptops_list = recommended_laptops.to_dict(orient='records')
        return recommended_laptops_list, web_recommended_laptops_info, input_info
    def get_sorted_web_products(web_recommended_laptops_info):
        combined_products = []

        # Kết hợp tất cả sản phẩm từ các DataFrame
        for web_dataframe in web_recommended_laptops_info:
            for product in web_dataframe:
                product['clean_discounted_price'] = float(product['discounted_price'].replace('₫','').replace('đ','').replace('.',''))
                combined_products.append(product)
        
        for product in combined_products:
            gift_count = sum(1 for key, value in product.items() if 'promotion' in key and not value != value)
            product['gift_count'] = gift_count
        
        # Sắp xếp sản phẩm theo giá tăng dần, sau đó theo số lượng promotion giảm dần
        sorted_web_products = sorted(combined_products, key=lambda x: (x['clean_discounted_price'], -x['gift_count']))
        return sorted_web_products
    
    # Gọi hàm để đề xuất laptop
    recommended_laptops_list, web_recommended_laptops_info, input_info = get_laptop_recommendations(propose= propose, price=price, brand= brand, size = size, color= color, weight = weight, material = material, cpu = cpu, ram = ram, hard_driver = hard_driver)
    sorted_web_products = get_sorted_web_products(web_recommended_laptops_info)

    return render_template('result.html', recommended_laptops_list=recommended_laptops_list, input_info=input_info, sorted_web_products=sorted_web_products)

if __name__ == '__main__':
    app.run(debug=True)
