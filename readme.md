# ๐๏ธ Semi Project โก

> ์๋น์ค ์ด๋ฆ : ์์ญ(SOONSAK)
>
> ์ ์ ๊ธฐ๊ฐ : 2022-11-09 ~ 2022-11-21
>
> ํ ๊ตฌ์ฑ : 16ํ SOONSAK (์ด๋์, ์ด์์ฒ , ๊ฐ๋ฌธ์ฃผ, ๋ฐ์์ค, ํ๊ฐ์, ์ด์๊ฒฝ)
>
> ๐ Link : http://soonsak-env.eba-rnwyi2s3.ap-northeast-2.elasticbeanstalk.com/



## ๐ award

20ํ ์ค ๊ณต๋ 4๋ฑ - ์์ฐจ์

<img src="readme.assets/award.png" alt="award" style="zoom:50%;" />



## ๐ซง Preview

- ๋ฉ์ธ ํ๋ฉด

<img src="readme.assets/221109-index.html.gif" alt="221109-index.html" style="zoom:50%;" />

- ๋ก๊ทธ์ธ

<img src="readme.assets/221109-login.html-0333576.gif" alt="221109-login.html" style="zoom:50%;" />

- ํ๋กํ ํ๋ฉด

<img src="readme.assets/221109-accounts-detail.html.gif" alt="221109-accounts-detail.html" style="zoom:50%;" />

- ์ฐ ๋ชฉ๋ก

<img src="readme.assets/221109-accounts-likelist.html.gif" alt="221109-accounts-likelist.html" style="zoom:50%;" />

- ์ํ ์์ธ ํ๋ฉด

<img src="readme.assets/221109-snacks-detail.html-reviews-detail.html.gif" alt="221109-snacks-detail.html-reviews-detail.html" style="zoom:50%;" />

- ์ฃผ๋ฌธ

<img src="readme.assets/221109-orders-create.html.gif" alt="221109-orders-create.html" style="zoom:50%;" />



## ๐ purpose

1. `Django` / `HTML` / `CSS` / `Javascript`์ ์ด์ฉํด `๊ตญ๋ด ๊ณผ์`, `ํด์ธ ๊ณผ์`, `์์  ๊ณผ์`๋ฅผ ๊ตฌ๋งคํ๊ณ  ๋ฆฌ๋ทฐ๋ฅผ ์์ฑํ  ์ ์๋ ์น ํ์ด์ง๋ฅผ ๊ตฌํ
2. ์ผ๋ฐ ์ฌ์ฉ์์ ๊ด๋ฆฌ์๋ฅผ ๊ตฌ๋ถํ์ฌ ์ฌ์ฉํ  ์ ์๋ ๊ธฐ๋ฅ์ ๋ถ๋ฆฌํจ
3. ์ค์ ๋ก ๊ฒฐ์ ํ  ์ ์๋๋ก ๊ฒฐ์  ํ๋ซํผ ๊ตฌํ



## โ๏ธ Stacks

<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Python-3776AB?stype=flat-square&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?stype=flat-square&logo=SQLite&logoColor=white"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=black"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>



## ๐ Description

1.   ๊ด๋ฆฌ์ ๊ณ์ ์ผ๋ก ๋ก๊ทธ์ธ์ ๋ชจ๋  ์ฃผ๋ฌธ๊ฑด์ ๊ด๋ฆฌํ  ์ ์๊ฒ ํจ

   - `orders/templates/orders/order_list.html`์์ ๋ชจ๋  ์ฃผ๋ฌธ ๋ด์ญ ์กฐํ ๊ฐ๋ฅ


   ```html
   <div class="row d-flex justify-content-center align-items-center py-5">
       <div class="d-flex flex-column justify-content-center align-items-center shadow p-5 rounded-5">
         <div class="bg-tape">
           <h1 class="d-flex justify-content-center">์ฃผ๋ฌธ๋ด์ญ</h1>
         </div>
         
   			<!-- ์ฃผ๋ฌธ๋ด์ญ ๊ด๋ฆฌ ๋ฒํผ -->
         <div class="container d-flex flex-column bg-white rounded-5 my-5">
           <div class="menu navbar-nav d-flex flex-row justify-content-center py-4">
             <li>
               <a type="button" id="complete_orders" class="pe-2 text-black">
                 <h5><i class="bi bi-credit-card"></i>๊ฒฐ์ ์๋ฃ</h5>
               </a>
             </li>/
             <li>
               <a type="button" id="delivery_orders" class="pe-2 text-black">
                 <h5><i class="bi bi-truck"></i>๋ฐฐ์ก๊ด๋ฆฌ</h5>
               </a>
             </li>/
             <li>
               <a type="button" id="cancel_orders" class="text-black">
                 <h5><i class="bi bi-x-circle"></i>์ทจ์์ฃผ๋ฌธ</h5>
               </a>
             </li>
           </div>
   
           <!-- ๊ฒฐ์  ์๋ฃ ๋ด์ญ -->
           <div id="completeOrders" style="display: none;">
             <div class="d-flex flex-column text-center mb-3">
               <h4 class="fw-bold">๊ฒฐ์ ์๋ฃ</h4>
               <table class="table text-center">
                 <thead>
                   <tr>
                     <th scope="col">No.</th>
                     <th scope="col">์ฃผ๋ฌธ์</th>
                     <th scope="col">์ํ</th>
                     <th scope="col">์๋</th>
                     <th scope="col">์ฃผ๋ฌธ๊ธ์ก(๋ฐฐ์ก๋น ๋ฏธํฌํจ)</th>
                     <th scope="col">๋ฐฐ์ก์ง</th>
                     <th scope="col">์ฐ๋ฝ์ฒ</th>
                     <th scope="col">์ฃผ๋ฌธ ์ํ</th>
                     <th scope="col">์ฃผ๋ฌธ ๋ ์ง</th>
                     <th scope="col">๋ฐฐ์ก ์ํ ๋ณ๊ฒฝ</th>
                   </tr>
                 </thead>
                 <tbody>
                   {% for order in complete_orders %}
                     <tr>
                       <td>{{ order.id }}</td>
                       <td>{{ order.user }}</td>
                       <td>{{ order.snack }}</td>
                       <td>{{ order.quantity }}</td>
                       <td>{{ order.total|intcomma }}์</td>
                       <td>{{ order.shipping_address }}</td>
                       <td>{{ order.contact_number }}</td>
                       <td>{{ order.order_status }}</td>
                       <td>{{ order.register_data }}</td>
                       <td class="d-grid gap-3 d-md-flex justify-content-center">
                         <a href="{% url 'orders:delete' order.pk %}" class="btn btn2" style="height: 27px;padding: 1px;width: 80px;">์ฃผ๋ฌธ์ทจ์</a>
                         <a href="{% url 'orders:delivery' order.pk %}" class="btn" style="height: 27px;padding: 1px;width: 80px;">๋ฐฐ์ก ์ค๋น์ค</a>
                       </td>
                     </tr>
                   {% endfor %}
                 </tbody>
               </table>
             </div>
           </div>
   ```

   > `๋ฐฐ์ก ์ค๋น์ค` / `๋ฐฐ์ก ์๋ฃ` / `์ฃผ๋ฌธ ์ทจ์` ๋ด์ญ๋ `๊ฒฐ์  ์๋ฃ` ๋ด์ญ๊ณผ ๋์ผํ๊ฒ ์ฝ๋ ๊ตฌ์ฑ

   - `orders/views.py`์ ํจ์ ์ถ๊ฐ

   ```python
   # ๋ฐฐ์ก ์ํ ๋ณ๊ฒฝ
   def delivery(request, order_pk):
       order = Order.objects.get(pk=order_pk)
       order.register_data = timezone.now()
       order.order_status = "๋ฐฐ์ก ์ค๋น์ค"
       order.save()
       return redirect("orders:order_list")
   
   # ๋ฐฐ์ก ์๋ฃ
   def delivery_complete(request, order_pk):
       order = Order.objects.get(pk=order_pk)
       order.register_data = timezone.now()
       order.order_status = "๋ฐฐ์ก์๋ฃ"
       order.save()
       return redirect("orders:order_list")
     
   # ๊ด๋ฆฌ์ ์ฃผ๋ฌธ ๋ด์ญ
   def order_list(request):
       # ๊ฒฐ์  ์๋ฃ๋ ์ฃผ๋ฌธ๋ค
       complete_orders = Order.objects.filter(order_status="๊ฒฐ์ ์๋ฃ").order_by("-register_data")
       # ์ทจ์๋ ์ฃผ๋ฌธ๋ค
       cancel_orders = Order.objects.filter(order_status="์ทจ์์ฃผ๋ฌธ").order_by("-register_data")
       # ๋ฐฐ์ก ์ค๋น์ค์ธ ์ฃผ๋ฌธ๋ค
       delivery_orders = Order.objects.filter(order_status="๋ฐฐ์ก ์ค๋น์ค").order_by("-register_data")
       # ๋ฐฐ์ก ์๋ฃ๋ ์ฃผ๋ฌธ๋ค
       delivery_complete_orders = Order.objects.filter(order_status="๋ฐฐ์ก์๋ฃ").order_by("-register_data")
       context = {
           "complete_orders": complete_orders,
           "cancel_orders": cancel_orders,
           "delivery_orders": delivery_orders,
           "delivery_complete_orders": delivery_complete_orders,
       }
       return render(request, "orders/order_list.html", context)
   ```

   - `orders/urls.py` ์ถ๊ฐ

   ```python
   # ๊ด๋ฆฌ์ ์ฃผ๋ฌธ ๋ด์ญ
   path('order_list/', views.order_list, name='order_list'),
   # ๋ฐฐ์ก ์ค๋น์ค
   path('delivery/<int:order_pk>/', views.delivery, name='delivery'),
   # ๋ฐฐ์ก ์๋ฃ
   path('delivery_complete/<int:order_pk>/', views.delivery_complete, name='delivery_complete')
   ```

   - `accounts/templates/accounts/detail.html`์ url ์ถ๊ฐ

   ```html
   <!-- ๊ด๋ฆฌ์๊ฐ ๊ด๋ฆฌ์ ํ๋กํ ์ ์ํ์๋๋ง ๋ณด์ด๋ ์นดํ๊ณ ๋ฆฌ/์ ํ๋ฑ๋ก ๋ฒํผ -->
   <div class="mt-3">
   	{% if request.user == user and request.user.is_staff %}
   		<!-- ์นดํ๊ณ ๋ฆฌ ๋ฑ๋ก -->
   		<a href="{% url 'snacks:category_create' %}" class="btn rounded-pill me-2" type="submit">์นดํ๊ณ ๋ฆฌ ๋ฑ๋ก</a>
       <!-- ์ ํ๋ฑ๋ก -->
       <a href="{% url 'snacks:create' %}" class="btn rounded-pill me-2" type="submit">์ ํ ๋ฑ๋ก</a>
       <!-- ์ฃผ๋ฌธ๋ด์ญ ๊ด๋ฆฌ -->
       <a href="{% url 'orders:order_list' %}" class="btn rounded-pill">์ฃผ๋ฌธ๋ด์ญ ๊ด๋ฆฌ</a>
     {% endif %}
   </div>
   ```

2. ํ์๊ฐ์ ๋ฐ ํ์์ ๋ณด ์์ ์ `์นด์นด์ค ์ฐํธ๋ฒํธ ์๋น์ค`๋ฅผ ์ด์ฉํด ๊ฒ์ ๊ธฐ๋ฅ ์ถ๊ฐ

3. - `accounts/templates/accounts/signup.html`

   ```html
   <div>
   	<input type="text" id="sample6_postcode" placeholder="์ฐํธ๋ฒํธ" name="postcode">
     <input class="btn rounded-pill" type="button" onclick="sample6_execDaumPostcode()" value="์ฐํธ๋ฒํธ ์ฐพ๊ธฐ"><br>
     <input type="text" id="sample6_address" placeholder="์ฃผ์" name="address"><br>
     <input type="text" id="sample6_detailAddress" placeholder="์์ธ์ฃผ์" name="detailAddress">
     <input type="text" id="sample6_extraAddress" name="extraAddress">
   </div>
   ```

   > `signup.html` ํ์ผ `{% block content %} ~ {% endblock %}` ์์ `script` ์ฝ๋ ์ถ๊ฐ ์์ฑ

   - `accounts/views.py` ์ ์ฝ๋ ์ถ๊ฐ

   ```python
   # ํ์๊ฐ์
   def signup(request):
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST, request.FILES)
           if form.is_valid():
               user = form.save(commit=False)
               user.address = request.POST.get('postcode') + request.POST.get('address') + request.POST.get('detailAddress') + request.POST.get('extraAddress')
               user.save()
   ...
       else:
           form = CustomUserCreationForm()
       context = {
           'form':form
       }
       return render(request, 'accounts/signup.html', context)
     
   # ํ์ ํ๋กํ ์์ 
   def update(request, user_pk):
   ...
               user.address = request.POST.get('postcode') + request.POST.get('address') + request.POST.get('detailAddress') + request.POST.get('extraAddress')
   ...
       return render(request, 'accounts/update.html', context)
   ```

3. ์์(`์นด์นด์ค`) ๋ก๊ทธ์ธ ์ฐ๋ ๊ตฌํ

   - `accounts/view.py`์ ํจ์ ์ถ๊ฐ

   ```python
   # ์นด์นด์ค ๋ก๊ทธ์ธ
   def kakao_request(request):
       kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
       redirect_uri = "http://soonsak-env.eba-rnwyi2s3.ap-northeast-2.elasticbeanstalk.com/accounts/login/kakao/callback"
       client_id = "e354ba53e1c46a96b9483564296d7ca9"  # ๋ฐฐํฌ์ ๋ณด์์ ์ฉ ํด์ผํจ
       return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")
   
   
   def kakao_callback(request):
       data = {
           "grant_type": "authorization_code",
           "client_id": "e354ba53e1c46a96b9483564296d7ca9",  # ๋ฐฐํฌ์ ๋ณด์์ ์ฉ ํด์ผํจ
           "redirect_uri": "http://soonsak-env.eba-rnwyi2s3.ap-northeast-2.elasticbeanstalk.com/accounts/login/kakao/callback",
           "code": request.GET.get("code"),
       }
       kakao_token_api = "https://kauth.kakao.com/oauth/token"
       access_token = requests.post(kakao_token_api, data=data).json()["access_token"]
   
       headers = {"Authorization": f"bearer ${access_token}"}
       kakao_user_api = "https://kapi.kakao.com/v2/user/me"
       kakao_user_information = requests.get(kakao_user_api, headers=headers).json()
   
       kakao_id = kakao_user_information["id"]
       kakao_nickname = kakao_user_information["properties"]["nickname"]
       # ์ ์  ๋ชจ๋ธ์ ํ๋กํ ์ฌ์ง ์ถ๊ฐ์ ์ฌ์ฉ
       kakao_profile_image = kakao_user_information["properties"]["profile_image"]
   
       if get_user_model().objects.filter(kakao_id=kakao_id).exists():
           kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
       else:
           kakao_login_user = get_user_model()()
           kakao_login_user.username = kakao_nickname
           kakao_login_user.kakao_id = kakao_id
           kakao_login_user.social_profile_picture = kakao_profile_image
           kakao_login_user.set_password(str(state_token))
           kakao_login_user.save()
           kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
       user_login(request, kakao_user, "django.contrib.auth.backends.ModelBackend")
       return redirect(request.GET.get("next") or "/")
   ```

   - `accounts/urls.py`

   ```python
   # ์นด์นด์ค ๋ก๊ทธ์ธ
   path("login/kakao/", views.kakao_request, name="kakao"),
   path("login/kakao/callback/", views.kakao_callback),
   ```

   - `accounts/login.html`์ ๋ก๊ทธ์ธ url ์ถ๊ฐ

   ```html
   <div class="mt-4">
   	<h4 class="d-flex justify-content-center">๊ฐํธ ๋ก๊ทธ์ธ</h4>
   	<div class="d-flex flex-column text-center mt-3">
       <a href="{% url 'accounts:login' %}kakao" class="mb-2">
       	<img src="{% static 'images/kakao_login.png' %}" alt="kakao">
       </a>
     </div>
   </div>
   ```

   



## ๐ฅ Issues

<details>
  <summary>makemigrations Pilkit ์ค๋ฅ</summary>
  <div markdown="1">
    <br>โ ์๋ฌ ์ฌํญ<br>โImportError: PILKit was unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.โ<br><br>
  </div>
  <div>
   ๐ก ํด๊ฒฐ๋ฐฉ๋ฒ<br>
    1. pip list ํด๋ณด๊ณ  pillow, image ๊ฐ ์ค์น ๋์ด์๋์ง ํ์ธํ๋ค.<br>
		2. ์๋ค๋ฉด ํฐ๋ฏธ๋์ sudo pip install pillow image<br>
		3. ์ค์น๋์ด ์๋ค๋ฉด  pip uninstall Pillow, pip uninstall Image<br>
		4. ๋ค์ pip install Pillow, pip install Image<br>
		5. pip uninstall Image ์๋๋ ๊ฒฝ์ฐ pip install Pillow ํ๋ค.<br>
		6. ๋ค์ makemigrations
  </div>
</details>

<details>
  <summary>'AnonymousUser' object has no attribute '_meta'</summary>
  <div markdown="1">
    <br>โ ์๋ฌ ์ฌํญ<br>
    ํ์๊ฐ์ ๊ธฐ๋ฅ ๊ตฌํ ํ ์๋ ๋ก๊ทธ์ธ ๊ธฐ๋ฅ์ ์ถ๊ฐํ์
		ํ์๊ฐ์์ด ์๋ฃ๋ ๋ค์ **['AnonymousUser' object has no attribute '_meta'](https://stackoverflow.com/questions/46284664/django-anonymoususer-object-has-no-attribute-meta) ์ค๋ฅ ๋ฐ์**<br><br>
  </div>
  <div markdown="1"> 
    ๐ก ํด๊ฒฐ ๋ฐฉ๋ฒ<br>
    1. py [manage.py](http://manage.py) makemigrations<br>
		2. py [manage.py](http://manage.py) migrate
  </div>
</details>
<details>
  <summary>Merge conflict</summary>
  <div markdown="1">
    <br>โ ์๋ฌ ์ฌํญ<br>
    ๊ฐ์ ํ์ผ์ ๋์์ ์์ํ๊ณ  push ๊ณผ์ ์์ ์ค๋ฅ ๋ฐ์<br><br>
  </div>
  <div markdown="1"> 
    ๐ก ํด๊ฒฐ ๋ฐฉ๋ฒ<br>
    1. ์๋ก clone์ ๋ฐ๊ณ  ์์<br>
		2. merge conflict ๋ฐ์ํ ๋ถ๋ถ์ ์์ 
  </div>
</details>



## ๐ซง Contributors

<a href="https://github.com/han-gaeul/SOONSAK/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=code-sum/SOONSAK" /></a>
