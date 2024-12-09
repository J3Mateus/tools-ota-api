from rest_framework import serializers

class WifiCreateInputSerializer(serializers.Serializer):
    SSDI = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)

    def validate_SSDI(self, value):
        """
        Valida o nome da rede (SSDI) para garantir que não seja vazio ou inválido.
        """
        if not value.strip():
            raise serializers.ValidationError("O nome da rede (SSDI) não pode estar vazio.")
        return value

    def validate_password(self, value):
        """
        Valida a senha para garantir que ela tenha pelo menos 8 caracteres.
        """
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value


class WifiUpdateInputSerializer(serializers.Serializer):
    SSDI = serializers.CharField(max_length=50, required=False)
    password = serializers.CharField(max_length=100, required=False)

    def validate(self, data):
        """
        Valida os dados de entrada para garantir consistência.
        """
        SSDI = data.get('SSDI')
        password = data.get('password')

        if SSDI is not None and not SSDI.strip():
            raise serializers.ValidationError("O nome da rede (SSDI) não pode estar vazio.")

        if password is not None and len(password) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        
        return data
