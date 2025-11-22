import streamlit as st
import base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
img1 = get_base64("assets/bg106.jpg")

abt_us_1 = '''A hobbyist who is trying to learn programming!<br>I'm contributing on backend stuff like how the game logic work, etc. also i'm good at C and Python.<br><br>My quote:<br>"I'm gonna find the truth."<br><br><br>'''

abt_us_2 = '''Gw ceplox21, alias murid yang namanya cuma sekata itu. Kontribusiku di sini ngerjain bagian <b>Frontend</b> karena aku sendiri dah lumayan paham dan ada pengalaman HTML sama CSS.<br><br>--- Quote kecil ---<br>"Don't be afraid of a rejection, because it's a path to success."<br><br><br>'''

def abt_us():
    st.markdown(
        '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&display=swap');
        </style>
        ''', unsafe_allow_html=True)

    st.html("""
        <style>
  /* From Uiverse.io by whoisyourdeadie */ 
  .matrix-container {
    position: relative;     /* stays on screen */
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;    /* NO scrolling allowed */
  }


  .matrix-pattern {
    position: relative;
    width: 1000px;
    height: 100%;
    flex-shrink: 0;
  }

  .matrix-column {
    position: absolute;
    top: -100%;
    width: 20px;
    height: 100%;
    font-size: 16px;
    line-height: 18px;
    font-weight: bold;
    animation: fall linear infinite;
    white-space: nowrap;
  }

  .matrix-column::before {
    content: "I'm going to fight, so I can keep my promise!";
    position: absolute;
    top: 0;
    left: 0;
    background: linear-gradient(
      to bottom,
      #ffffff 0%,
      #ffffff 5%,
      #00ff41 10%,
      #00ff41 20%,
      #00dd33 30%,
      #00bb22 40%,
      #009911 50%,
      #007700 60%,
      #005500 70%,
      #003300 80%,
      rgba(0, 255, 65, 0.5) 90%,
      transparent 100%
    );
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    writing-mode: vertical-lr;
    letter-spacing: 1px;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .matrix-column:nth-child(1) {
    left: 0px;
    animation-delay: -2.5s;
    animation-duration: 3s;
  }
  .matrix-column:nth-child(2) {
    left: 25px;
    animation-delay: -3.2s;
    animation-duration: 4s;
  }
  .matrix-column:nth-child(3) {
    left: 50px;
    animation-delay: -1.8s;
    animation-duration: 2.5s;
  }
  .matrix-column:nth-child(4) {
    left: 75px;
    animation-delay: -2.9s;
    animation-duration: 3.5s;
  }
  .matrix-column:nth-child(5) {
    left: 100px;
    animation-delay: -1.5s;
    animation-duration: 3s;
  }
  .matrix-column:nth-child(6) {
    left: 125px;
    animation-delay: -3.8s;
    animation-duration: 4.5s;
  }
  .matrix-column:nth-child(7) {
    left: 150px;
    animation-delay: -2.1s;
    animation-duration: 2.8s;
  }
  .matrix-column:nth-child(8) {
    left: 175px;
    animation-delay: -2.7s;
    animation-duration: 3.2s;
  }
  .matrix-column:nth-child(9) {
    left: 200px;
    animation-delay: -3.4s;
    animation-duration: 3.8s;
  }
  .matrix-column:nth-child(10) {
    left: 225px;
    animation-delay: -1.9s;
    animation-duration: 2.7s;
  }
  .matrix-column:nth-child(11) {
    left: 250px;
    animation-delay: -3.6s;
    animation-duration: 4.2s;
  }
  .matrix-column:nth-child(12) {
    left: 275px;
    animation-delay: -2.3s;
    animation-duration: 3.1s;
  }
  .matrix-column:nth-child(13) {
    left: 300px;
    animation-delay: -3.1s;
    animation-duration: 3.6s;
  }
  .matrix-column:nth-child(14) {
    left: 325px;
    animation-delay: -2.6s;
    animation-duration: 2.9s;
  }
  .matrix-column:nth-child(15) {
    left: 350px;
    animation-delay: -3.7s;
    animation-duration: 4.1s;
  }
  .matrix-column:nth-child(16) {
    left: 375px;
    animation-delay: -2.8s;
    animation-duration: 3.3s;
  }
  .matrix-column:nth-child(17) {
    left: 400px;
    animation-delay: -3.3s;
    animation-duration: 3.7s;
  }
  .matrix-column:nth-child(18) {
    left: 425px;
    animation-delay: -2.2s;
    animation-duration: 2.6s;
  }
  .matrix-column:nth-child(19) {
    left: 450px;
    animation-delay: -3.9s;
    animation-duration: 4.3s;
  }
  .matrix-column:nth-child(20) {
    left: 475px;
    animation-delay: -2.4s;
    animation-duration: 3.4s;
  }
  .matrix-column:nth-child(21) {
    left: 500px;
    animation-delay: -1.7s;
    animation-duration: 2.4s;
  }
  .matrix-column:nth-child(22) {
    left: 525px;
    animation-delay: -3.5s;
    animation-duration: 3.9s;
  }
  .matrix-column:nth-child(23) {
    left: 550px;
    animation-delay: -2s;
    animation-duration: 3s;
  }
  .matrix-column:nth-child(24) {
    left: 575px;
    animation-delay: -4s;
    animation-duration: 4.4s;
  }
  .matrix-column:nth-child(25) {
    left: 600px;
    animation-delay: -1.6s;
    animation-duration: 2.3s;
  }
  .matrix-column:nth-child(26) {
    left: 625px;
    animation-delay: -3s;
    animation-duration: 3.5s;
  }
  .matrix-column:nth-child(27) {
    left: 650px;
    animation-delay: -3.8s;
    animation-duration: 4s;
  }
  .matrix-column:nth-child(28) {
    left: 675px;
    animation-delay: -2.5s;
    animation-duration: 2.8s;
  }
  .matrix-column:nth-child(29) {
    left: 700px;
    animation-delay: -3.2s;
    animation-duration: 3.6s;
  }
  .matrix-column:nth-child(30) {
    left: 725px;
    animation-delay: -2.7s;
    animation-duration: 3.2s;
  }
  .matrix-column:nth-child(31) {
    left: 750px;
    animation-delay: -1.8s;
    animation-duration: 2.7s;
  }
  .matrix-column:nth-child(32) {
    left: 775px;
    animation-delay: -3.6s;
    animation-duration: 4.1s;
  }
  .matrix-column:nth-child(33) {
    left: 800px;
    animation-delay: -2.1s;
    animation-duration: 3.1s;
  }
  .matrix-column:nth-child(34) {
    left: 825px;
    animation-delay: -3.4s;
    animation-duration: 3.7s;
  }
  .matrix-column:nth-child(35) {
    left: 850px;
    animation-delay: -2.8s;
    animation-duration: 2.9s;
  }
  .matrix-column:nth-child(36) {
    left: 875px;
    animation-delay: -3.7s;
    animation-duration: 4.2s;
  }
  .matrix-column:nth-child(37) {
    left: 900px;
    animation-delay: -2.3s;
    animation-duration: 3.3s;
  }
  .matrix-column:nth-child(38) {
    left: 925px;
    animation-delay: -1.9s;
    animation-duration: 2.5s;
  }
  .matrix-column:nth-child(39) {
    left: 950px;
    animation-delay: -3.5s;
    animation-duration: 3.8s;
  }
  .matrix-column:nth-child(40) {
    left: 975px;
    animation-delay: -2.6s;
    animation-duration: 3.4s;
  }

  .matrix-column:nth-child(odd)::before {
    content: "Every human has regrets, has things they'd like to go back and change. But I don't! 'cause I'm a bear.";
  }

  .matrix-column:nth-child(even)::before {
    content: "I'm so glad everyone is so thoughtful toward their friends...! Hehehe, we're all equals when we're sick. Let's all work together and do our very best.";
  }

  .matrix-column:nth-child(3n)::before {
    content: "If you want to believe in someone...you need to overcome doubt first. Belief without doubt...is simply a lie.";
  }

  .matrix-column:nth-child(4n)::before {
    content: "I never erase a photo once I take it. That's my policy. No matter what kind of photo it is, the moment captured in it only exists at that time.";
  }

  .matrix-column:nth-child(5n)::before {
    content: "Over the years, my show has given many smiles to people with broken hearts... Now is the time to demonstrate my powers. My magic is the only thing that can heal your twisted hearts.";
  }

.expandable-info:not(:hover) .matrix-wrapper .matrix-container .matrix-pattern .matrix-column {
animation-play-state: paused;
}
.expandable-info:not(:hover) .matrix-wrapper .jp-matrix span {
animation-play-state: paused;
}

  @keyframes fall {
    0% {
      transform: translateY(-10%);
      opacity: 1;
    }
    100% {
      transform: translateY(150%);
      opacity: 0;
    }
  }


  @media (max-width: 768px) {
    .matrix-column {
      font-size: 14px;
      line-height: 16px;
      width: 18px;
    }
  }

  @media (max-width: 480px) {
    .matrix-column {
      font-size: 12px;
      line-height: 14px;
      width: 15px;
    }
  }

        </style>""")

    st.html(
        f"""
        <div class="maincontainer bbh-sans-bogle-regular">
            <div class="container-h1">
                <h1>TENTANG KAMI</h1>
            </div>
            <div class="divider-container">
                <div class="divider"></div>
            </div>
        </div>

        <div class="maincontainer">
                <div class="imagecontainer1">
                    <img src="https://avatars.githubusercontent.com/u/95009791?v=4">
                </div>
                <div class="expandable-info">
                    <div class="desktop-only"><div class="info-title1 momo-trust-display-regular">Hover mouse ke sini!</div></div>
                    <div class="mobile-only"><div class="info-title1 momo-trust-display-regular">Pencet ke sini!</div></div>
                    <div class="matrix-wrapper">
                        <div class="jp-matrix">
                        <span>最</span><span>終</span><span>防</span><span>衛</span><span>学</span><span>園</span><span>-</span
                        ><span>ハ</span><span>ン</span><span>ド</span><span>レ</span><span>ッ</span><span>ド</span><span>ラ</span><span>イ</span><span>ン</span
                        ><span>最</span><span>終</span><span>防</span><span>衛</span><span>学</span><span>園</span><span>-</span
                        ><span>ハ</span><span>ン</span><span>ド</span><span>レ</span><span>ッ</span><span>ド</span><span>ラ</span><span>イ</span><span>ン</span
                        ><span>最</span><span>終</span><span>防</span><span>衛</span><span>学</span><span>園</span><span>-</span
                        ><span>ハ</span><span>ン</span><span>ド</span><span>レ</span><span>ッ</span><span>ド</span><span>ラ</span><span>イ</span><span>ン</span
                        </div></div>
                        <div class="blur-box"><div class="overlay arima-isi">{abt_us_1}</div>
                        </div>
                    </div>
                </div>
            <div class="divider-container2">
                <div class="divider"></div>
            </div>
                <div class="imagecontainer2">
                    <img src="https://avatars.githubusercontent.com/u/230108871?v=4">
                </div>
                <div class="expandable-info">
                    <div class="desktop-only"><div class="info-title2 momo-trust-display-regular">Hover mouse ke sini!</div></div>
                    <div class="mobile-only"><div class="info-title2 momo-trust-display-regular">Pencet ke sini!</div></div>
                    <div class="matrix-wrapper">
                      <div class="matrix-container">
                        <div class="matrix-pattern">
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                          <div class="matrix-column"></div>
                        </div>
                      </div>
                      <div class="blur-box"><div class="overlay arima-isi">{abt_us_2}</div>
                    </div>
                </div>
        </div>

       <style>
            .blur-box {{
            position: absolute;
            z-index: 2;
            top: 0;
            backdrop-filter: blur(2px);
            -webkit-backdrop-filter: blur(2px); /* for Safari */
            background: rgba(0, 0, 0, 0.3); /* transparent enough to show blur */
            border-radius: .5rem;
            padding: 2rem;
            justify-content: center;
            }}

            .matrix-wrapper {{
            position: relative;       /* creates a positioning context */
            }}

            .overlay {{
            top: -20px;
            position: relative;
            z-index: 10;              /* above jp-matrix */
            color: white;
            pointer-events: none;     /* optional: don't block mouse */
            font-size: 1em;
            }}

            .jp-matrix {{
            position: absolute;
            inset: 0;                 /* fill wrapper */
            z-index: 1;               /* behind overlay */
            position: relative;
            background-color: transparent;
            overflow: hidden;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
            grid-auto-rows: 60px;
            font-size: 42px;
            color: rgba(0, 150, 255, 0.4);
            font-family: "Courier New", Courier, monospace;
            justify-content: center;
            align-content: center;
            }}

            .jp-matrix > span {{
            text-align: center;
            text-shadow: 0 0 5px rgba(0, 150, 255, 0.5);
            user-select: none;
            transition:
                color 0.5s,
                text-shadow 0.5s;
            line-height: 1;
            }}

            .jp-matrix > span:nth-child(19n + 2) {{
            animation: smooth-pulse 3.5s ease-in-out infinite 0.2s;
            }}
            .jp-matrix > span:nth-child(29n + 1) {{
            animation: smooth-pulse 4.1s ease-in-out infinite 0.7s;
            }}
            .jp-matrix > span:nth-child(11n) {{
            color: rgba(100, 200, 255, 0.7);
            animation: smooth-pulse 2.9s ease-in-out infinite 1.1s;
            }}
            .jp-matrix > span:nth-child(37n + 10) {{
            animation: smooth-pulse 5.3s ease-in-out infinite 1.5s;
            }}
            .jp-matrix > span:nth-child(41n + 1) {{
            animation: smooth-pulse 3.9s ease-in-out infinite 0.4s;
            }}
            .jp-matrix > span:nth-child(17n + 9) {{
            animation: smooth-pulse 2.8s ease-in-out infinite 0.9s;
            }}
            .jp-matrix > span:nth-child(23n + 18) {{
            animation: smooth-pulse 4.3s ease-in-out infinite 1.3s;
            }}
            .jp-matrix > span:nth-child(31n + 4) {{
            animation: smooth-pulse 5.6s ease-in-out infinite 0.1s;
            }}
            .jp-matrix > span:nth-child(43n + 20) {{
            animation: smooth-pulse 3.6s ease-in-out infinite 1.8s;
            }}
            .jp-matrix > span:nth-child(13n + 6) {{
            animation: smooth-pulse 3.2s ease-in-out infinite 1.2s;
            }}
            .jp-matrix > span:nth-child(53n + 5) {{
            animation: smooth-pulse 4.9s ease-in-out infinite 0.5s;
            }}
            .jp-matrix > span:nth-child(47n + 15) {{
            animation: smooth-pulse 5.9s ease-in-out infinite 1s;
            }}

            @keyframes smooth-pulse {{
            0%,
            100% {{
                color: rgba(0, 150, 255, 0.4);
                text-shadow: 0 0 5px rgba(0, 150, 255, 0.5);
            }}
            30% {{
                color: rgba(100, 200, 255, 1);
                text-shadow:
                0 0 10px rgba(100, 200, 255, 1),
                0 0 15px rgba(100, 200, 255, 1);
            }}
            50% {{
                color: rgba(255, 105, 180, 1);
                text-shadow:
                0 0 10px rgba(255, 105, 180, 1),
                0 0 15px rgba(255, 105, 180, 1);
            }}
            70% {{
                color: #cf2b4a;
                text-shadow:
                0 0 10px #cf2b4a,
                0 0 15px #cf2b4a,
                0 0 20px #cf2b4a;
            }}
            }}

            .grand-container {{
            display: flex;
            }}

            .keterangan {{
            max-width: 80%;
            margin: 1.5em;
            }}

            .imagecontainer1, .imagecontainer2 {{
            position: relative;
            }}
            .imagecontainer1::before, .imagecontainer2::before {{
            position: absolute;
            background-color: #4858A8;
            padding: .1em .25em;
            border-radius: 5px;
            transform: translate(-50%);
            left: 50%;
            border: 5px solid #6674BD;
            font-weight: bold;
            }}
            .imagecontainer1::before {{
            content: "Molimen (X-6/13)";
            }}
            .imagecontainer2::before {{
            content: "Ceplox21 (X-6/18)";
            }}
            .imagecontainer1 img, .imagecontainer2 img {{
            box-sizing: border-box;
            margin: 1em 1em 2.1em 1em;
            height: 9.25em;
            aspect-ratio: 16:9;
            border: 5px solid #6674BD;
            border-radius: 1.25em 0em 2.65em 0em;
            }}

            .info-content {{
            margin: 1.25em;
            font-size: 1em;
            }}

            .info-title1::after {{
            content: "Info Tentang Molimen";
            }}
            .info-title2::after {{
            content: "Info Tentang Ceplox21";
            }}
            .info-title1::after, .info-title2::after {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: row;
            background-color: #D38D2C;
            height: 105%;
            width: 0%;
            z-index: 3;
            top: 50%;
            left: -40%;
            transform: translate(0%, -50%);
            position: absolute;
            transition: all .9s ease;
            overflow: hidden;
            white-space: nowrap;
            font-size: 1.38rem;

            }}
            .expandable-info:hover .info-title1::after, .expandable-info:hover .info-title2::after {{
            width: 180%;
            transition: all .9s ease;
            }}

            .expandable-info {{
            display: flex;
            flex-direction: column;
            height: 3em;
            width: 80%;
            background-color: #353536;
            max-width: 90%;
            margin-bottom: 2em;
            border-radius: .5rem;
            transition: all .35s ease;
            border: 0.2rem solid #24ADF2;
            overflow: hidden;
            }}
            .expandable-info:hover {{
            height: 20em;
            transition: all .35s ease-out;
            border: 0.2rem solid #996620;
            }}

            .expandable-info .info-title1, .expandable-info .info-title2 {{
            padding: .18em;
            font-size: 1.42em;
            background-color: #66a0bd;
            transition: all .5s ease-out;
            position: relative;
            }}

            .stApp {{
            background-color: #232324;
            background-position: center top;
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
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

            .maincontainer, .maincontainer2 {{
            color: white;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            }}

            .container-h1 {{
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            width: 90%;
            padding: 1px;
            position: relative;
            z-index: 1;
            }}

            .container-h1::before, .container-h1::after {{
            content: "";
            width: 200px;
            height: 100%;
            position: absolute;
            background-color: #232324;
            z-index: 12;
            filter: blur(.8em);
            }}

            .container-h1::after {{
            content: "";
            opacity: 1;
            transform: translate(-127%, 0);
            }}
            .container-h1::before {{
            content: "";
            opacity: 1;
            transform: translate(127%, 0);
            }}

            h1 {{
            font-size: 5em;
            letter-spacing: 4px;
            z-index: 10;
            background-image: url(data:image/jpg;base64,{img1});
            background-position: top center;
            background-size: cover;
            background-repeat: no-repeat;
            padding: 25px 135px;
            text-align: center;
            line-height: 1em;
            border: 4px solid lightblue;
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

            body {{
            user-select: none;
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

            @media (max-width: 700px) {{
                .info-content {{
                font-size: 0.85em;
                margin: .95em;
                }}
                .info-title1::after, .info-title2::after {{
                font-size: 0.85em;
                }}
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
        """)
