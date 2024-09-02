# AutoGen Ajanları ve Kod Yönetimi

Bu proje, `autogen` kütüphanesini kullanarak yazılım geliştirme sürecini simüle etmek ve farklı rollerdeki ajanları (yönetici, yazılımcı, testçi) yönetmek için hazırlanmıştır. 

## Proje İçeriği

- **Manager**: Geliştirme sürecini yöneten ve planları onaylayan ajan.
- **Developer**: Onaylı planlara göre kod yazan ve kodu diske kaydeden ajan.
- **Tester**: Geliştirilen kodu test eden, hataları raporlayan ve otomatik test betikleri oluşturan ajan.

## Gereksinimler

- `autogen` ve `litellm` kütüphaneleri
- CodeLlama modeline erişim

## Kurulum

1. Python ortamınızı oluşturun ve gerekli paketleri yükleyin:
    ```bash
    pip install autogen==1.0.16
    pip install litellm
    ```

2. `CodeLlama` modelini kurun:
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ollama run codellama
    litellm --model ollama/codellama
    ```

   Not: Eğer bağlanma hatası alırsanız, aşağıdaki adımları izleyin:
    ```bash
    python -m site --user-base
    export PATH=$PATH:/home/Username/.local/bin
    echo 'export PATH=$PATH:/home/Username/.local/bin' >> ~/.bashrc
    source ~/.bashrc
    ```

## Kod Yapısı

### Yapılandırma

`config_list_codellama` değişkeni, CodeLlama modelinin yapılandırma ayarlarını içerir. Modelin çalıştığı sunucu adresi ve API anahtarı gibi bilgileri içerir.

### Ajanlar

- **Yönetici Ajanı (Manager)**: Geliştirme sürecini yöneten ve onaylayan ajandır.
- **Yazılımcı Ajanı (Developer)**: Onaylı planlara göre kod yazan ajandır.
- **Testçi Ajanı (Tester)**: Yazılımcının kodunu test eden ve hataları raporlayan ajandır.

### Grup Sohbeti

`GroupChat` sınıfı, ajanların etkileşimde bulunmasını sağlar. Sohbetin maksimum tur sayısı 12 olarak ayarlanmıştır.

## Kullanım

Proje, grup sohbetini başlatmak ve yönetici ajanın yazılımcıya belirli bir görev vermesiyle çalışır. Örneğin, yönetici ajanın yazılımcıya 0 ile 100 arasındaki asal sayıları yazdıran bir Python kodu yazmasını istemesi gibi.
