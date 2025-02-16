from src.session_state import SessionState


class global_test_static:
    session_state = SessionState

    def __init__(self):
        global_test_static.session_state.template_name = "global_test_static"


class test_static_1:
    session_state = SessionState

    def __init__(self):
        self.session_state.template_name = "test_static_1"


print(f"Valor: {SessionState.template_name} -> Valor deve ser 'Initial Template' indicando que a varável inicia com o valor esperado.")

global_test_static()
print(f"\nValor: {SessionState.template_name} -> Valor deve ser 'global_test_static' pois foi instanciada a classe global_test_static.")

test_static_1()
print(f"\nValor: {SessionState.template_name} -> Valor deve ser 'test_static_1' pois foi instanciada a classe test_static_1.")