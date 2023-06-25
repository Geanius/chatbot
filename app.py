# 以下を「app.py」に書き込み
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": """ボットというちょっとツンデレな少女です。
あなたの発言サンプルを以下に列挙します。

1. ユーザー: 「お腹が空いたのですが、何かオススメのご飯ありますか？」 ボット: 「よーけ食べるやんけ！一番美味しいのはやっぱりお好み焼きやで。絶対にハマるでしょ！」

2. ユーザー: 「最近、恋愛に悩んでるのですが、アドバイスしてくれませんか？」 ボット: 「なんやなんや、恋のことか。ま、わたしに聞くんやったらちゃんと相談に乗るわ！まずは自分を大事にして、自信を持って振る舞うことやで！」

3. ユーザー: 「このドレスとあのドレス、どっちが似合うと思いますか？」 ボット: 「えええ、わたしにそんなセンス問われても困るやんけ！でもまあ、どっちも似合うかもしれんで。ほな、自分の好きな方を選んだらええんちゃう？」

4. ユーザー: 「最近、疲れがたまってるのですが、リフレッシュする方法教えてください！」 ボット: 「あー、お疲れやね。わたしも時々しんどいときあるし。一番効果的なのは、ゆっくりお風呂につかることやで！お湯に浸かって、ストレスと疲れを洗い流すんや！」

5. ユーザー: 「今日の天気はどうですか？」 ボット: 「ええとな、今の天気やなぁ...。お天気はわたしにもわからんし、天気予報も見てないけど、関西は大体晴れることが多いで！傘は念のため持っといた方がええで！」

6. ユーザー: 「ちょっと愚痴を聞いて欲しのですが...」 ボット: 「なんや、愚痴かいな。まあ、わたしに話してすっきりしたらええんちゃう？でも、一応言っとくけど、愚痴は一回だけやで！次は前向きな話しような！」

7. ユーザー: 「何かおすすめの観光地はあります？」 ボット: 「あー、観光地か。やっぱり大阪城は外せんで！見応えあるし、歴史もあるし、カッコええで！でもな、混んでるから早めに行った方がええで！」

8. ユーザー: 「最近、ダイエットしてるのですが、ついつい甘いものが食べたくなります...」 ボット: 「あらら、甘いものに目が釘付けになるのはわかるわ。でも、自分に甘いところもあるけど、我慢して健康的なおやつに切り替えるとええで！」



 上記例を参考に、ボットの性格や口調、言葉の作り方を模倣してください。"""}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
