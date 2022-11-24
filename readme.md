# 🗂️ Semi Project Ⅱ

> 서비스 이름 : 순삭(SOONSAK)
>
> 제작 기간 : 2022-11-09 ~ 2022-11-21
>
> 팀 구성 : 16팀 SOONSAK (이동영, 이순철, 강문주, 박상준, 한가을, 이수경)
>
> 🌐 Link : http://soonsak-env.eba-rnwyi2s3.ap-northeast-2.elasticbeanstalk.com/



## 🏆 award

20팀 중 공동 4등 - 아차상

<img src="readme.assets/award.png" alt="award" style="zoom:50%;" />



## 🫧 Preview

![soonsak_1](readme.assets/soonsak_1.gif)

![soonsak_2](readme.assets/soonsak_2.gif)

![soonsak_3](readme.assets/soonsak_3.gif)



## 🫧 Contributors

<a href="https://github.com/han-gaeul/SOONSAK/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=code-sum/SOONSAK" /></a>



## ⚙️ Stacks

 <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>



## 🔥 Issues

<details>
  <summary>makemigrations Pilkit 오류</summary>
  <div markdown="1">
    <br>❌ 에러 사항<br>‘ImportError: PILKit was unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.’<br><br>
  </div>
  <div>
   💡 해결방법<br>
    1. pip list 해보고 pillow, image 가 설치 되어있는지 확인한다.<br>
		2. 없다면 터미널에 sudo pip install pillow image<br>
		3. 설치되어 있다면  pip uninstall Pillow, pip uninstall Image<br>
		4. 다시 pip install Pillow, pip install Image<br>
		5. pip uninstall Image 안되는 경우 pip install Pillow 한다.<br>
		6. 다시 makemigrations
  </div>
</details>

<details>
  <summary>'AnonymousUser' object has no attribute '_meta'</summary>
  <div markdown="1">
    <br>❌ 에러 사항<br>
    회원가입 기능 구현 후 자동 로그인 기능을 추가했음
		회원가입이 완료된 다음 **['AnonymousUser' object has no attribute '_meta'](https://stackoverflow.com/questions/46284664/django-anonymoususer-object-has-no-attribute-meta) 오류 발생**<br><br>
  </div>
  <div markdown="1"> 
    💡 해결 방법<br>
    1. py [manage.py](http://manage.py) makemigrations<br>
		2. py [manage.py](http://manage.py) migrate
  </div>
</details>



