import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ekstra1 = get_base64("assets/extra_img1.jpg")
ekstra2 = get_base64("assets/extra_img2.png")
img1 = get_base64("assets/extra_img3.png")


def extra_menu():
    st.markdown("""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&display=swap');            
                </style>
                """, unsafe_allow_html=True)

    st.html("""<style>
.containter_card {
  position: relative;
  width: 190px;
  height: 254px;
  transition: 200ms;
}

.containter_card:active {
  width: 180px;
  height: 245px;
}

#card {
position: absolute;
inset: 0;
z-index: 0;
display: flex;
justify-content: center;
align-items: center;
border-radius: 20px;
transition: 700ms;
border: 3px solid rgba(0, 0, 0, 1);
overflow: hidden;
box-shadow:
    0 0 20px rgba(0, 0, 0, 0.3),
    inset 0 0 20px rgba(0, 0, 0, 0.2);
}

.card-content {
  position: relative;
  width: 100%;
  height: 100%;
}

#prompt {
  bottom: 40%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 20;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 2px;
  transition: 300ms ease-in-out;
  position: absolute;
  text-align: center;
  color: rgb(255, 255, 255);
  border-radius: 10px; border: 3px solid rgba(36, 173, 242, 0.3); background-color: rgba(102, 160, 189, 0.67); font-size: 20px;padding:1px;
}

.title_card {
  opacity: 0;
  transition: 300ms ease-in-out;
  position: absolute;
  text-align: center;
  width: 100%;
  padding: 20px 20px 0px 20px;
}

.subtitle {
  position: absolute;
  bottom: 40px;
  width: 100%;
  text-align: center;
  font-size: 12px;
  letter-spacing: 2px;
  transform: translateY(30px);
  color: rgba(255, 255, 255, 1);
}

.highlight {
  color: #00ffaa;
  margin-left: 5px;
  background: linear-gradient(90deg, #5c67ff, #ad51ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}

/* Hover effects */
.tracker:hover ~ #card .title_card {
  opacity: 1;
  transform: translateY(-10px);
}

#card::before {
  content: "";
  filter: blur(20px);
  opacity: 0;
  width: 150%;
  height: 150%;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  transition: opacity 0.3s ease;
}

.tracker:hover ~ #card::before {
  opacity: 1;
}

.tracker {
  position: absolute;
  z-index: 200;
  width: 100%;
  height: 100%;
}

.tracker:hover {
  cursor: pointer;
}

.tracker:hover ~ #card #prompt {
  opacity: 0;
}

.tracker:hover ~ #card {
  transition: 300ms;
}

.containter_card:hover #card::before {
  transition: 200ms;
  content: "";
  opacity: 80%;
}

.canvas {
  perspective: 800px;
  inset: 0;
  z-index: 200;
  position: absolute;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
  gap: 0px 0px;
  grid-template-areas:
    "tr-1 tr-2 tr-3 tr-4 tr-5"
    "tr-6 tr-7 tr-8 tr-9 tr-10"
    "tr-11 tr-12 tr-13 tr-14 tr-15"
    "tr-16 tr-17 tr-18 tr-19 tr-20"
    "tr-21 tr-22 tr-23 tr-24 tr-25";
}

.tr-1 {
  grid-area: tr-1;
}

.tr-2 {
  grid-area: tr-2;
}

.tr-3 {
  grid-area: tr-3;
}

.tr-4 {
  grid-area: tr-4;
}

.tr-5 {
  grid-area: tr-5;
}

.tr-6 {
  grid-area: tr-6;
}

.tr-7 {
  grid-area: tr-7;
}

.tr-8 {
  grid-area: tr-8;
}

.tr-9 {
  grid-area: tr-9;
}

.tr-10 {
  grid-area: tr-10;
}

.tr-11 {
  grid-area: tr-11;
}

.tr-12 {
  grid-area: tr-12;
}

.tr-13 {
  grid-area: tr-13;
}

.tr-14 {
  grid-area: tr-14;
}

.tr-15 {
  grid-area: tr-15;
}

.tr-16 {
  grid-area: tr-16;
}

.tr-17 {
  grid-area: tr-17;
}

.tr-18 {
  grid-area: tr-18;
}

.tr-19 {
  grid-area: tr-19;
}

.tr-20 {
  grid-area: tr-20;
}

.tr-21 {
  grid-area: tr-21;
}

.tr-22 {
  grid-area: tr-22;
}

.tr-23 {
  grid-area: tr-23;
}

.tr-24 {
  grid-area: tr-24;
}

.tr-25 {
  grid-area: tr-25;
}

.tr-1:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-2:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-3:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(0deg) rotateZ(0deg);
}

.tr-4:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(5deg) rotateZ(0deg);
}

.tr-5:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(10deg) rotateZ(0deg);
}

.tr-6:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-7:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-8:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(0deg) rotateZ(0deg);
}

.tr-9:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(5deg) rotateZ(0deg);
}

.tr-10:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(10deg) rotateZ(0deg);
}

.tr-11:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-12:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-13:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
}

.tr-14:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(5deg) rotateZ(0deg);
}

.tr-15:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(10deg) rotateZ(0deg);
}

.tr-16:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-17:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-18:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(0deg) rotateZ(0deg);
}

.tr-19:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(5deg) rotateZ(0deg);
}

.tr-20:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(10deg) rotateZ(0deg);
}

.tr-21:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-22:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-23:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(0deg) rotateZ(0deg);
}

.tr-24:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(5deg) rotateZ(0deg);
}

.tr-25:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(10deg) rotateZ(0deg);
}

.noselect {
  -webkit-touch-callout: none;
  /* iOS Safari */
  -webkit-user-select: none;
  /* Safari */
  /* Konqueror HTML */
  -moz-user-select: none;
  /* Old versions of Firefox */
  -ms-user-select: none;
  /* Internet Explorer/Edge */
  user-select: none;
  /* Non-prefixed version, currently
									supported by Chrome, Edge, Opera and Firefox */
}

@keyframes scanMove {
  0% {
    transform: translateY(-100%);
  }
  100% {
    transform: translateY(100%);
  }
}
            </style>""")

    st.html(f"""  
        <style>
        .card_img1 {{
        background-image: url(data:image/jpg;base64,{ekstra1});
        background-position: center;
        background-size: cover;
        }}

        .card_img2 {{
        background-image: url(data:image/jpg;base64,{ekstra2});
        background-position: center;
        background-size: cover;
        }}

        * {{
        user-select: none;
        }}
        .momo-trust-display-regular {{
        font-family: "Momo Trust Display", sans-serif;
        font-weight: 400;
        font-style: normal;
        }}
        .bbh-sans-bogle-regular {{
            font-family: "BBH Sans Bogle", sans-serif;
            font-weight: 400;
            font-style: normal;
        }}
        .arima-isi {{
            font-family: "Arima", system-ui;
            font-optical-sizing: auto;
            font-weight: 500;
            font-style: normal;
            line-height: 1.75em;
        }}

        .stApp {{
            background-image: linear-gradient(0deg, #242424, #232324);
            background-position: center top;
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
        }}

        .container-h1 {{
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding: 1px;
        position: relative;
        z-index: 1;
        margin: 0;
        }}
        
        .container-h1::before, .container-h1::after {{
        content: "";
        width: 180px;
        height: 95%;
        position: absolute;
        background-color: #232324;
        z-index: 12;
        filter: blur(.8em);
        }}
        
        .container-h1::after {{
        content: "";
        opacity: 1;
        transform: translate(-140%, 0);
        }}
        .container-h1::before {{
        content: "";
        opacity: 1;
        transform: translate(140%, 0);
        }}
        
        h1 {{
        font-size: 6em;
        letter-spacing: 4px;
        z-index: 10;
        background-image: url(data:image/jpg;base64,{img1});
        background-position: left;
        background-size: cover;
        background-repeat: no-repeat;
        padding: 65px .7em;
        text-align: center;
        line-height: 1em;
        border: 4px solid lightblue;
        color: white;
        }}
        
        p {{
            color: white;
        }}
        .container, .container2 {{
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            max-width: 100%;
            margin: 0;
            flex-wrap: wrap;
            height: 100%;
            position: relative;
        }}
        
        .img1 {{
                width: 15em;
                height: 16em;
                z-index: 6;
                border-radius: 10px;
                }}

                .imgcontainer {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                position: relative;
                margin: 0 auto;
                border-radius: 10px;
                z-index: 5;
                overflow: hidden;
                padding: 8px;
                }}
                .imgcontainer::after, .imgcontainer::before {{
                content: "";
                width: 150%;
                position: absolute;
                height: 150%;
                background-image: conic-gradient(from 90deg, #ff8080, transparent, transparent,transparent, #809dff, transparent,transparent,transparent, #ff8080);
                z-index: 0;
                padding: 15px;
                border-radius: 10px;
                animation: 15s rotatebg linear infinite;
                }}
                .imgcontainer::before{{
                content: "";
                filter: blur(2em);
                opacity: 0;
                }}
                
        .img2 {{
                width: 15em;
                height: 16em;
                z-index: 6;
                border-radius: 10px;
                }}

                .imgcontainer2 {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                position: relative;
                margin: 0 auto;
                border-radius: 10px;
                z-index: 5;
                overflow: hidden;
                padding: 8px;
                }}
                .imgcontainer2::after, .imgcontainer2::before {{
                content: "";
                width: 200%;
                position: absolute;
                height: 200%;
                background-image: conic-gradient(from 0deg, #ffff80, transparent, transparent,transparent, #86ff80, transparent,transparent,transparent, #ffff80);
                z-index: 0;
                padding: 10px;
                border-radius: 10px;
                overflow: hidden;
                animation: 13s rotatebg linear infinite;
                }}
                .imgcontainer2::before{{
                    filter: blur(1em);
                }}

                @keyframes rotatebg {{
                    from {{
                        transform: rotate(0deg);
                    }}
                    to {{
                        transform: rotate(360deg);
                    }}
                }}

        a {{
            text-decoration: none;
            font-weight: bold;
            color: black;
            padding: 0.75em 5em;
            z-index: 5;
            font-size: 1em;
        }}
        
        .linkbtn {{ 
        margin: 1em 1em 1em 1em;
        border-radius: 99px;
        background-color: #8346bd;
        border: 4px solid #7102d9;
        padding: 10px 0;
        position: relative;
        overflow: hidden;
        transition: all .5s ease;
        box-sizing: border-box;
        }}
        .linkbtn::before, .linkbtn::after {{
        content: "";
        position: absolute;
        width: 100%;
        height: 120%;
        top: -10%;
        z-index: 0;
        pointer-events: none;
        transition: all .5s ease;
        }}
        .linkbtn::before {{
        left: 110%;
        transform: skewX(-30deg);
        }}
        .linkbtn::after {{
        left: -110%;
        transform: skewX(30deg);
        }}
        .linkbtn:has(a:hover)::before {{
        transform: translateX(-70%) skewX(-45deg);
        transition: all .5s ease .05s;
        background-color: #43de7b;
        }}
        .linkbtn:has(a:hover)::after {{
        transform: translateX(70%) skewX(45deg);
        transition: all .5s ease .05s;
        background-color: #43de7b;
        }}
        .linkbtn:has(a:hover) {{
        border: 4px solid #23a151;  
        transition: all .5s ease;
        }}
        
        .after-hover {{
        font-size: 2em;
        display: block;
        background-color: transparent;
        height: 1.5em;
        width: 3em;
        position: absolute;
        left: 35%;
        top: 120%;
        transform: translate(-40% -50%);
        z-index: 6;
        letter-spacing: 0.3rem;
        text-align: center;
        transition: all .2s ease;
        color: black;
        }}
        .linkbtn:has(a:hover) .after-hover {{
        transform: translateY(-120%);
        transition: all .5s ease 0.2s;
        pointer-events: none;
        }}
        
        
        .title {{
            font-size: 2.1em;
            color: white;
            margin-bottom: 15px;
        }}
        
        .divider-container, .divider-container2 {{
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 1px;
                z-index: 1;
                width: 100%;
                height: .5rem;
                position: relative;
                margin: 3em;
                margin-top: 1.25em;
                }}
                
                .divider-container::before, .divider-container::after, .divider-container2::before, .divider-container2::after {{
                transition: all 1s ease;
                }}
                .divider-container::before {{
                content: "";
                top: -197%;
                width: 40px;
                height: 40px;
                background-color: #232324;
                position: absolute;
                transform: rotate(45deg);
                animation: bg-divider-scale 7s ease-out infinite;
                }}
                .divider-container2::before {{
                content: "";
                content: "";
                top: -197%;
                width: 40px;
                height: 40px;
                background-color: #232324;
                position: absolute;
                transform: rotate(45deg);
                animation: bg-divider-scale 7s ease-out reverse infinite;
                }}
                .divider-container::after {{
                content: "";
                width: 20px;
                height: 20px;
                background-color: white;
                position: absolute;
                transform: rotate(45deg);
                animation: divider-spin 7s ease infinite;
                }}
                .divider-container2::after {{
                content: "";
                width: 20px;
                height: 20px;
                background-color: white;
                position: absolute;
                transform: rotate(45deg);
                animation: divider-spin 7s ease reverse infinite;
                }}
                .divider {{
                height: .35rem;
                width: 100%;
                background-image: linear-gradient(90deg, transparent, white,white, transparent);
                margin: 1.5em;
                }}
        
        .textcontainer {{
        border-radius: 10px;
        border: 3px solid black;
        background-color: #383839;
        margin: 1.25em;
        line-height: 2.25em;
        padding: 10px 10px 0px 10px;
        max-width: 90%;
        }}
        
        .grand-imgcontainer {{
        text-align: center;
        width: 100%;
        }}
        
        @keyframes colorchange {{
            33% {{ background-color: #91b4eb; }}
            66% {{ background-color: #dae5f7; }}
        }}
        
        @media (min-width: 700px) {{
            .container, .container2 {{
            display: flex;
            align-items: center;
            text-align: center;
            padding: 0;
            justify-content: center;
            margin: 0;
            }}
            .container {{
            float: left;
            flex-wrap: wrap;
            flex-direction: row;
            }}
            .container2 {{
            float: right;
            flex-wrap: wrap;
            flex-direction: row-reverse;
            }}
            
            .imgcontainer {{
            text-align: center;
            float: left;
            }}
            
            .textcontainer {{
            max-width: 50%;
            }}
        }}
        
        @keyframes divider-spin {{
                0% {{ transform: rotate(0deg); }}
                5.88% {{ transform: rotate(0deg); }}
                11.76% {{ transform: rotate(45deg); }}
                17.64% {{ transform: rotate(45deg); }}
                23.52% {{ transform: rotate(90deg); }}
                29.4% {{ transform: rotate(90deg); }}
                35.28% {{ transform: rotate(135deg); }}
                41.16% {{ transform: rotate(135deg); }}
                47.04% {{ transform: rotate(180deg); }}
                52.92% {{ transform: rotate(180deg); }}
                58.8% {{ transform: rotate(225deg); }}
                64.68% {{ transform: rotate(225deg); }}
                70.56% {{ transform: rotate(270deg); }}
                76.44% {{ transform: rotate(270deg); }}
                82.32% {{ transform: rotate(315deg); }}
                88.2% {{ transform: rotate(315deg); }}
                100% {{ transform: rotate(360deg); }}
                }}
            @keyframes bg-divider-scale {{
                0% {{ transform:  scale(1); }}
                5.88% {{ transform:  scale(1); }}
                11.76% {{ transform:  scale(1.25); }}
                17.64% {{ transform:  scale(1.25); }}
                23.52% {{ transform:  scale(1); }}
                29.4% {{ transform:  scale(1); }}
                35.28% {{ transform:  scale(1.25); }}
                41.16% {{ transform:  scale(1.25); }}
                47.04% {{ transform:  scale(1); }}
                52.92% {{ transform:  scale(1); }}
                58.8% {{ transform:  scale(1.25); }}
                64.68% {{ transform:  scale(1.25); }}
                70.56% {{ transform:  scale(1); }}
                76.44% {{ transform:  scale(1); }}
                82.32% {{ transform:  scale(1.25); }}
                88.2% {{ transform: scale(1.25); }}
                94.08% {{ transform: scale(1); }}
                100% {{ transform: scale(1); }}
                }}

            @media (max-width: 768px) {{
                .mobile-only {{display: block;}}
                .desktop-only {{display: none;}}
            }}
            @media (min-width: 769px) {{
                .mobile-only {{display: none;}}
                .desktop-only {{display: block;}}
            }}
        </style>
        
        <div class="container-h1 bbh-sans-bogle-regular">
            <h1>EKSTRA</h1>
        </div>
        
        <div class="container"> 
            <div class="divider-container">
                <div class="divider"></div>
            </div>
            <div style="display: flex; justify-content: center;">
            <div class="containter_card noselect">
            <div class="canvas">
                <div class="tracker tr-1"></div>
                <div class="tracker tr-2"></div>
                <div class="tracker tr-3"></div>
                <div class="tracker tr-4"></div>
                <div class="tracker tr-5"></div>
                <div class="tracker tr-6"></div>
                <div class="tracker tr-7"></div>
                <div class="tracker tr-8"></div>
                <div class="tracker tr-9"></div>
                <div class="tracker tr-10"></div>
                <div class="tracker tr-11"></div>
                <div class="tracker tr-12"></div>
                <div class="tracker tr-13"></div>
                <div class="tracker tr-14"></div>
                <div class="tracker tr-15"></div>
                <div class="tracker tr-16"></div>
                <div class="tracker tr-17"></div>
                <div class="tracker tr-18"></div>
                <div class="tracker tr-19"></div>
                <div class="tracker tr-20"></div>
                <div class="tracker tr-21"></div>
                <div class="tracker tr-22"></div>
                <div class="tracker tr-23"></div>
                <div class="tracker tr-24"></div>
                <div class="tracker tr-25"></div>
                <div id="card" class="card_img1">
                <div class="card-content">
                    <div id="prompt"><div class="bbh-sans-bogle-regular desktop-only">HOVER ME!</div><div class="bbh-sans-bogle-regular mobile-only">PRESS ME!</div></div>
                </div>
                </div>
            </div>
            </div>
            </div>
            <div class="textcontainer">
                <div class="title momo-trust-display-regular">Tempat Duduk Generator</div>
                <p class="arima-isi">Ini program yang bisa dipake untuk ngatur tempat duduk secara otomatis dengan cowo-cewe selang-seling. Untuk sekarang ini cuma bisa untuk kelas 10, soalnya gw ga ada database buat kelas 11 ama 12.</p>
            </div>
            <span class="linkbtn">
                <a href="https://layout-tempat-duduk-generator.streamlit.app/" target="_blank">Kunjungi situsnya</a>
                <span class="after-hover bbh-sans-bogle-regular">KLIK!</span>
            </span>
        </div>

        <div class="container2">   
            <div class="divider-container2">
                <div class="divider"></div>
            </div>
            <div style="display: flex; justify-content: center;">
            <div class="containter_card noselect">
            <div class="canvas">
                <div class="tracker tr-1"></div>
                <div class="tracker tr-2"></div>
                <div class="tracker tr-3"></div>
                <div class="tracker tr-4"></div>
                <div class="tracker tr-5"></div>
                <div class="tracker tr-6"></div>
                <div class="tracker tr-7"></div>
                <div class="tracker tr-8"></div>
                <div class="tracker tr-9"></div>
                <div class="tracker tr-10"></div>
                <div class="tracker tr-11"></div>
                <div class="tracker tr-12"></div>
                <div class="tracker tr-13"></div>
                <div class="tracker tr-14"></div>
                <div class="tracker tr-15"></div>
                <div class="tracker tr-16"></div>
                <div class="tracker tr-17"></div>
                <div class="tracker tr-18"></div>
                <div class="tracker tr-19"></div>
                <div class="tracker tr-20"></div>
                <div class="tracker tr-21"></div>
                <div class="tracker tr-22"></div>
                <div class="tracker tr-23"></div>
                <div class="tracker tr-24"></div>
                <div class="tracker tr-25"></div>
                <div id="card"  class="card_img2">
                <div class="card-content">
                    <div id="prompt"><div class="bbh-sans-bogle-regular desktop-only">HOVER ME!</div><div class="bbh-sans-bogle-regular mobile-only">PRESS ME!</div></div>
                </div>
                </div>
            </div>
            </div>
            </div>
            <div class="textcontainer">
                <div class="title momo-trust-display-regular">Kelompok Generator</div>
                <p class="arima-isi">Program yang bisa mbuat kelompok, tapi fitur jumlah cowo sama cewe tiap kelompok dibagi sama rata secara otomatis ini bikin unik. Ini juga cuma bisa untuk kelas 10 dulu. </p>
            </div>
            <span class="linkbtn">
                <a href="https://kelompok.streamlit.app/" target="_blank">Kunjungi situsnya</a>
                <span class="after-hover bbh-sans-bogle-regular">KLIK!</span>
            </span>
        </div>
        
    """)





