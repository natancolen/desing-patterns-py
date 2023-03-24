class Target:
    """
    O Target define a interface específica do domínio usada pelo código do cliente.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."
class Adaptee:
    """
    O Adaptee contém algum comportamento útil, mas sua interface é incompatível
    com o código de cliente existente. O Adaptado precisa de alguma adaptação antes do
    o código do cliente pode usá-lo.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    O Adaptador torna a interface do Adaptee compatível com a do Target
    interface via herança múltipla.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    O código Client suporta todas as classes que seguem a interface Target.
    """

    print(target.request(), end="")


if __name__ == '__main__':
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)

