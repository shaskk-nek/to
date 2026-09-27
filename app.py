from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Một lá thư dành cho Bà 💌</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: Georgia, "Times New Roman", serif;

    background:
        radial-gradient(circle at top, #fff7fa, transparent 45%),
        linear-gradient(135deg, #ffd8e5, #eadcff);

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 25px 12px;

    color: #5c3c48;

    overflow-x: hidden;
}

/* =========================
   TIM BAY
========================= */

.hearts {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
}

.heart {
    position: absolute;
    bottom: -50px;

    font-size: 22px;

    animation: fly 8s linear infinite;

    opacity: 0.7;
}

.heart:nth-child(1) {
    left: 8%;
    animation-delay: 0s;
}

.heart:nth-child(2) {
    left: 28%;
    animation-delay: 2s;
}

.heart:nth-child(3) {
    left: 50%;
    animation-delay: 4s;
}

.heart:nth-child(4) {
    left: 72%;
    animation-delay: 1s;
}

.heart:nth-child(5) {
    left: 90%;
    animation-delay: 3s;
}

@keyframes fly {

    0% {
        transform:
            translateY(0)
            rotate(0deg);

        opacity: 0;
    }

    20% {
        opacity: 0.8;
    }

    100% {
        transform:
            translateY(-110vh)
            rotate(360deg);

        opacity: 0;
    }
}


/* =========================
   CONTAINER
========================= */

.container {
    width: 100%;
    max-width: 450px;

    text-align: center;

    position: relative;
    z-index: 2;
}


/* =========================
   PHONG BÌ
========================= */

.envelope {

    position: relative;

    width: 100%;
    height: 280px;

    background: #fff;

    border-radius: 12px;

    box-shadow:
        0 20px 45px
        rgba(100, 50, 70, 0.23);

    overflow: hidden;

    transition:
        0.8s ease;
}


/* phần thân phong bì */

.envelope-body {

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            135deg,
            #ffd1df,
            #f7b5ca
        );

    z-index: 1;
}


/* =========================
   NẮP PHONG BÌ
========================= */

.flap {

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    background: #f2a8bf;

    clip-path:
        polygon(
            0 0,
            50% 53%,
            100% 0
        );

    z-index: 6;

    transform-origin: top;

    transition:
        transform 0.9s ease,
        opacity 0.7s ease;
}


/* =========================
   HAI MÉP PHONG BÌ
========================= */

.left-fold {

    position: absolute;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 70%;

    background: #efa0b9;

    clip-path:
        polygon(
            0 100%,
            50% 35%,
            0 0
        );

    z-index: 4;
}


.right-fold {

    position: absolute;

    right: 0;
    bottom: 0;

    width: 100%;
    height: 70%;

    background: #e994b0;

    clip-path:
        polygon(
            100% 100%,
            50% 35%,
            100% 0
        );

    z-index: 4;
}


/* =========================
   ĐÁY PHONG BÌ
========================= */

.bottom-fold {

    position: absolute;

    bottom: 0;
    left: 0;

    width: 100%;
    height: 55%;

    background: #f7b1c8;

    clip-path:
        polygon(
            0 100%,
            50% 20%,
            100% 100%
        );

    z-index: 5;
}


/* =========================
   LÁ THƯ BÊN TRONG
========================= */

.letter {

    position: absolute;

    left: 6%;
    bottom: 5%;

    width: 88%;
    height: 82%;

    background: #fffdf8;

    border-radius: 8px;

    padding: 25px 20px;

    box-shadow:
        0 5px 15px
        rgba(0,0,0,0.08);

    z-index: 2;

    overflow: hidden;

    transition:
        0.9s ease;
}


/* =========================
   NỘI DUNG THƯ
========================= */

.content {

    opacity: 0;

    transform:
        translateY(20px);

    transition:
        1s ease;
}

.content h2 {

    margin-top: 0;
    margin-bottom: 20px;

    color: #d4577c;

    font-size: 25px;
}

.content p {

    font-family: Arial, sans-serif;

    font-size: 16px;

    line-height: 1.8;

    text-align: left;

    margin: 0 0 17px 0;

    white-space: pre-line;

    word-wrap: break-word;
}

.signature {

    margin-top: 25px;

    text-align: right;

    font-style: italic;

    color: #c14f72;

    font-size: 16px;
}


/* =========================
   CON DẤU TIM
========================= */

.seal {

    position: absolute;

    left: 50%;
    top: 52%;

    transform:
        translate(-50%, -50%);

    width: 70px;
    height: 70px;

    border: none;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 30%,
            #f38ca9,
            #d94f78
        );

    color: white;

    font-size: 29px;

    cursor: pointer;

    z-index: 10;

    box-shadow:
        0 8px 22px
        rgba(160, 50, 90, 0.35);

    transition:
        0.3s;
}

.seal:hover {

    transform:
        translate(-50%, -50%)
        scale(1.1);
}


/* =========================
   CHƯA MỞ
========================= */

.hint {

    margin-top: 20px;

    font-size: 15px;

    line-height: 1.6;

    color: #825465;
}


/* =========================
   ĐÃ MỞ
========================= */

.opened .flap {

    transform:
        rotateX(180deg);

    opacity: 0;
}

.opened .left-fold,
.opened .right-fold,
.opened .bottom-fold,
.opened .envelope-body {

    opacity: 0;
}

.opened .envelope {

    height: auto;

    min-height: 0;

    overflow: visible;

    padding: 15px;

    background: transparent;

    box-shadow: none;
}

.opened .letter {

    position: relative;

    left: 0;
    bottom: auto;

    width: 100%;

    height: auto;

    min-height: 300px;

    overflow: visible;

    padding: 30px 22px;

    box-shadow:
        0 12px 35px
        rgba(90, 50, 70, 0.18);
}

.opened .content {

    opacity: 1;

    transform:
        translateY(0);
}

.opened .seal {

    opacity: 0;

    pointer-events: none;
}


/* =========================
   NÚT ĐÓNG
========================= */

.close-btn {

    margin-top: 20px;

    border: none;

    border-radius: 30px;

    padding:
        11px 25px;

    background: #d9577c;

    color: white;

    font-size: 14px;

    cursor: pointer;

    box-shadow:
        0 5px 15px
        rgba(150, 50, 80, 0.2);
}


/* =========================
   ĐIỆN THOẠI
========================= */

@media (max-width: 480px) {

    body {

        align-items: flex-start;

        padding-top: 45px;
    }

    .envelope {

        height: 250px;
    }

    .letter {

        padding:
            23px 17px;
    }

    .content h2 {

        font-size: 23px;
    }

    .content p {

        font-size: 15px;

        line-height: 1.75;
    }
}

</style>
</head>


<body>


<div class="hearts">

    <div class="heart">💗</div>
    <div class="heart">♡</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">♡</div>

</div>



<div class="container" id="app">


    <!-- PHONG BÌ -->

    <div class="envelope">


        <div class="envelope-body"></div>


        <div class="letter">

            <div class="content">

                <h2>
                    Gửi Bà 💗
                </h2>


                <p>
Nghe tin cậu bị tai nạn, tớ thật sự rất lo. 🥺
Không biết bây giờ cậu đã đỡ đau hơn chưa, sức khỏe thế nào rồi. Tớ chỉ mong cậu không bị thương quá nặng và mọi thứ đang dần ổn hơn.

Mấy ngày này cậu nhớ nghỉ ngơi thật nhiều nha. Đừng cố gắng làm những việc khiến cơ thể mệt thêm, ăn uống đầy đủ và nhớ làm theo lời bác sĩ nữa. 🌷

Tớ biết đôi khi sau một chuyện như vậy, người ta sẽ dễ mệt mỏi và buồn hơn bình thường. Nhưng cậu đừng lo quá nhé, cứ từ từ hồi phục. Không cần phải vội vàng trở lại như trước đâu, sức khỏe của cậu mới là điều quan trọng nhất.

Tớ cũng chẳng biết mình có thể giúp được gì nhiều, nên chỉ có thể gửi cậu vài lời hỏi thăm như thế này. Mong rằng mỗi ngày cậu sẽ khỏe hơn một chút, bớt đau một chút và sớm có thể trở lại với những ngày bình thường. 💗

Nhớ giữ gìn sức khỏe nha.
Mong cậu mau khỏe, và nhất định phải vui vẻ trở lại đó. 🫶🏻🌸

— Một người thật lòng lo cho cậu 💕
                </p>


                <div class="signature">

                    — Người viết lá thư này 💌

                </div>

            </div>

        </div>



        <div class="left-fold"></div>

        <div class="right-fold"></div>

        <div class="bottom-fold"></div>

        <div class="flap"></div>


        <!-- CON DẤU -->

        <button
            class="seal"
            onclick="openLetter()">

            ❤

        </button>


    </div>



    <div
        class="hint"
        id="hint">

        Có một lá thư dành riêng cho cậu...
        <br>

        <b>
            Chạm vào trái tim để mở 💌
        </b>

    </div>



    <button
        class="close-btn"
        id="closeBtn"
        onclick="closeLetter()"
        style="display:none;">

        Đóng thư

    </button>


</div>



<script>

function openLetter() {

    document
        .getElementById("app")
        .classList.add("opened");


    document
        .getElementById("hint")
        .innerHTML =
        "Một chút tâm tình dành riêng cho cậu 💗";


    document
        .getElementById("closeBtn")
        .style.display =
        "inline-block";


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}



function closeLetter() {

    document
        .getElementById("app")
        .classList.remove("opened");


    document
        .getElementById("hint")
        .innerHTML =
        "Có một lá thư dành riêng cho cậu..." +
        "<br><b>" +
        "Chạm vào trái tim để mở 💌" +
        "</b>";


    document
        .getElementById("closeBtn")
        .style.display =
        "none";


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}

</script>


</body>
</html>
"""


@app.route("/")
def home():

    return render_template_string(HTML)


if __name__ == "__main__":

    print("")
    print("💌 LÁ THƯ ĐANG CHẠY...")
    print("")
    print("🌷 Mở trình duyệt:")
    print("http://127.0.0.1:5000")
    print("")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )