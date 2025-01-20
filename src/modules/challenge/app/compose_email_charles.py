
def compose_email_charles(pic_64: str):
    message = """
    
<!DOCTYPE html>
        <html lang="pt-br" charset="UTF-8">
        <head>
        </head>
        <body style="margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: white; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
        <table class="main" style="width: 50vw; max-width: 600px; background-color: white; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25); overflow: hidden;">
            <tr>
            <td>
                <table class="TittleBox" style="width: 100%; background-color: #110e47; border-radius: 10px 10px 0 0;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <h1 style="color: #ffffff; margin-top: 10px;"><strong>Desafio 1</strong></h1>
                    </td>
                </tr>
                </table>
                <table class="ContentBox" style="width: 100%; background-color: #282470; border-top: 1px solid #ffffff; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="word-wrap: break-word;">
                        <h2 style="color: #ffffff;">Olá, Mateus!! Segue a foto que o Charleszinho queria... será que você irá receber isso?</p></h2>
                        <img alt="Desenho do Charles" src="data:image/png;base64, {pic_64}" style="width: 100%;"/>
                    </div>
                    </td>
                </tr>
                </table>
                <table class="BottomBox" style="width: 100%; background-color: #110e47; border-top: 1px solid #ffffff; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="color: #ffffff; word-wrap: break-word;">
                        <h2>Atenciosamente,</h2>
                        <h2><strong>Vitin de Férias</strong>&#127744;</h2>
                    </div>
                    </td>
                </tr>
                </table>
            </td>
            </tr>
        </table>
        </body>
        </html>


"""

    message = message.format(pic_64=pic_64)

    return message