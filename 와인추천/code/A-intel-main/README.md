# A-Intel
분명한 기호를 선택하여 와인을 추천받는다!
Choose a clear preference and get a wine recommendation!

- 어느 가격대를 원하세요? (가볍게 마실 데일리 와인! / 다른 사람과 마실 선물용 와인! / 이 좋은 와인은 나혼자 마셔야해! 고급 와인!)
- 어느 국가를 선호하세요? 
- Light / Bold?
- Smooth / Tannic?
- Dry / Sweet?
- Soft / Acidic?

A-Intel 와인추천시스템에서 확실한 와인 추천 경험을 즐기세요.
Enjoy an authentic wine recommendation experience with the A-Intel Wine Recommendation System.

### [A-Intel](https://a-intel.vercel.app/)


## Members

| 20141113 | 20152365 | 20161851 |
| --- | --- | --- |
| [김일혁](https://github.com/illlama) | [백동훈](https://github.com/Ada4489) | [조민수](https://github.com/jjominsoo) |
|<img src="https://github.com/illlama.png" width="80"> | <img src="https://github.com/Ada4489.png" width="80"> | <img src="https://github.com/jjominsoo.png" width="80"> |



### 역할 분담

김일혁 - FE
조민수, 백동훈 - BE

### 프로세스!
BE
1. kaggle 데이터를 가져와 데이터베이스를 구축한다.
2. 와인 리스트는 평점순으로 정렬하여 적당히 2000개 고른다.
3. [light / bold] [smooth / tannic] [soft / acidic] [dry / sweet] 값을 가져온다.
4. 사용자의 카테고리에 맞는 와인을 추천해주고, 사용자 평가를 가지고 데이터셋을 업데이트해준다.

FE
1. 시작 페이지에서 부터 선호하는 것을 고르면서 넘어간다.
2. 가격 국가 [맛 4가지] 를 선택한다.
3. 카테고리에 맞는 와인을 추천해준다.
4. 사용자는 이 와인에 대해 평가한다.
5. (옵션) 비비노에서 최근평점순으로 나열하여 랜덤한 평점을 가져온다.

### 기술스텍
-FE : React
-BE : MySQL, Django

### 일자별 진행 사항
11월 첫째주
- 프로세스 확정
- 역할 분담
- 깃헙 정리
- 스텍 확정
- 차주 과제 분담 (~11월 11일까지)
- 조민수, 백동훈 : 공부 및 데이터셋 준비
- 김일혁 : 개발환경 세팅 및 와이어프레임 작성
----- 
### 11월 둘째주 (11.11 회의)
이번주 진행 사항
- FE : 디자인 완료, 초기 환경 설정 완료
- React의 SSR를 위해 Next.js 사용하기로 변경했습니다. (검색 결과에 뜨는게 좋고, 페이지 이동이 거의 없기에 SSR이 유리하다고 생각합니다)
- BE : DB관리를 위한 공동 tool 결정 (mySQL), 효율을 위한 데이터처리 분업 역할 배정
- 백동훈 : mySQL을 이용하여 kaggle에서 얻은 와인데이터셋을 DB에 저장
- 조민수 : DB에서 와인명을 읽어 vivino에서 해당하는 와인의 맛(feature)에 관한 데이터 수집
- ++ 고객의 평점을 데이터셋에 반영하는 작업 (미정)

차주 목표
- FE : 디자인 나온 것들 레이아웃 / 랜딩페이지, Question 페이지 완성
- BE : DB에 데이터 저장 및 처리 / DB 데이터 활용
둘째주 기념사진 촬영 📸
![스크린샷 2021-11-11 오후 2 30 25](https://user-images.githubusercontent.com/13018853/141242933-f1c444f5-bd35-44ee-b5cd-e5efdae950ca.png)

### 11월 셋째주 (11.18 회의)
이번주 진행 사항
- FE : 화면 레이아웃 구성, Select하는 부분까지 페이지 넘어가도록 구현, 배포 (https://a-intel.vercel.app/)
- BE : 크롤링에 쓰기 위한 데이터 가공처리, 가공된 데이터(와인명) 바탕으로 해당하는 페이지 연결

차주 목표
- FE : 기호 조사를 완료 후 json 형태로 BE에 넘기기
- BE : 연결된 페이지로부터 맛에 관한 정보들 받아 데이터 업데이트 하기

셋째주 기념사진 촬영 📸
![스크린샷 2021-11-18 오후 1 57 32](https://user-images.githubusercontent.com/13018853/142750223-b0a6022a-83cd-41d0-b887-6f7fa08ff5a4.png)


### 11월 넷째주 (11.25 회의)
이번주 진행 사항
- FE : 기호 조사 완료! 약간의 애니메이션 추가, css 조정
![ezgif com-gif-maker](https://user-images.githubusercontent.com/13018853/143727651-77e08a27-33ec-4b95-a382-8321c8c9cd06.gif)
- BE : 기존 사이트에서 크롤링이 안된다는 문제점을 파악하고 다른 방법 모색 > winesearcher를 이용하기로 함, 추천 알고리즘 확립

차주 목표
- FE : BE API와 연결해서 결과값 전송하고, 받아오기 + 결과 페이지
- BE : 새로운 사이트에서 크롤링 완료, 알고리즘 구현

셋째주 기념사진 촬영 📸
<img width="1430" alt="스크린샷 2021-11-25 오후 7 07 46" src="https://user-images.githubusercontent.com/13018853/143727646-af58fb77-6924-4c17-9758-c509b6087c49.png">


### 12월 첫째주 (12.02 회의)
이번주 진행 사항
- FE : 기획 변경에 따른 선호도 조사 방법 변화
- BE : 크롤링 진행중 (허가오류 해결중), 추천방식의 구체화, 데이터 2차 가공

차주 목표
- FE : 버그픽스
- BE : 크롤링 완료, 가중치 설정, 추가 추천시스템 확인


### 12월 둘째주 (12.09 회의)
이번주 진행 사항
- FE : 버그픽스
- BE : 
및
발표 준비

-----



## #Idea 회의 기록

데이터처리
데이터를 받아온다 > 받아오는 데이터 인자들 설명
추가할만한 인자들?
평점을 노멀라이즈

기법
사용자는 초기 서비스 이용할때 질문을 받아서 사용자의 답변에 기반하여 사용자의 성향을 분석하여 알맞은 와인 추천 >> 어떤 답을 받을지?
예) 좋아하는 음식 / 좋아하는 맛 / 결혼 했는지 / 등등 
유사한 사람의 와인 선호도 제공
어떻게 보여줄지? >> 
>> 추가적으로 우리만의 기능들 설명

평가방법
>> 와인 마다 구매사이트를 링크를 걸어두고 그 링크에 들어가면 관심을 보인다고 파악하자.


## 디자인

# Landing
![Landing](https://user-images.githubusercontent.com/13018853/141241959-d1e7e9cb-b7fc-4f2f-b199-1b987ae30e94.jpg)
# Question
![Question](https://user-images.githubusercontent.com/13018853/141241967-4969cece-7ae4-4708-a50a-4ffd4308a3b7.jpg)
![Question Copy](https://user-images.githubusercontent.com/13018853/141241981-d7db66e3-3824-44a9-b293-c24fae277c92.jpg)
![Question Copy 5](https://user-images.githubusercontent.com/13018853/141242014-017f77eb-f082-4234-8486-3a832db7f7ec.jpg)
![Question Copy 4](https://user-images.githubusercontent.com/13018853/141242021-8c2586d3-015f-4e4f-9f79-eab1e40b90b7.jpg)
![Question Copy 3](https://user-images.githubusercontent.com/13018853/141242026-df4d715d-10f0-4984-851f-1ed2db9d5cd4.jpg)
![Question Copy 2](https://user-images.githubusercontent.com/13018853/141242030-52a24ebc-2a82-4e4d-84d6-0292e03c25f5.jpg)
# Result
![result](https://user-images.githubusercontent.com/13018853/141242047-d3315e5e-e503-4370-9d1c-fd783059ef83.jpg)


