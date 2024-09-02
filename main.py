import autogen  

# CodeLlama modeli için yapılandırma ayarları
config_list_codellama = [
    {
        'base_url': "http://0.0.0.0:4000 ",  # Modelin çalıştığı sunucu adresi
        'api_key': "NULL",  # API anahtarı
        'model': 'ollama/codellama'  # Kullanılan modelin adı
    }
]

# LLM yapılandırma ayarları
llm_config = {
    "cache_seed": 43,  # Önbellekleme işlemleri için kullanılan rastgelelik tohumu
    "config_list": config_list_codellama  # Model yapılandırmalarını içeren liste
}

# Yönetici Ajanı
manager = autogen.UserProxyAgent(
    name="Manager",  # Ajanın adı
    # Yönetici ajanın sistemi tanımlayan mesajı, ajanın rolünü açıklar.
    system_message="A manager. Manages the development process and approves plans. Oversees the project progress.",
    max_consecutive_auto_reply=5,  # Maksimum otomatik cevap sayısı
    code_execution_config={
        "work_dir": "code",  # Kodun çalıştırılacağı çalışma dizini
        "use_docker": False  # Docker kullanımı devre dışı
    },
    human_input_mode="NEVER",  # İnsan girdisi gereksinimi yok, otomatik çalışıyor
    # Ajanın görevini sonlandırması için mesajın 'TERMINATE' ile bitmesi gerekiyor
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)

# Yazılımcı Ajanı
developer = autogen.AssistantAgent(
    name="Developer",  
    llm_config=llm_config, 
    system_message="""Developer. Follows the approved plan and writes code to implement features. Save code to disk. 
    Use best practices in coding and document the code where necessary.""",
)

# Testçi Ajanı
tester = autogen.AssistantAgent(
    name="Tester", 
    llm_config=llm_config,  
    system_message="""Tester. Tests the code developed by the developer. Identifies bugs and reports them back.
    Creates automated test scripts and ensures code quality.""",
)

# Grup Sohbeti ve Yönetici

# Yönetici, yazılımcı ve testçiyi içeren bir grup sohbeti oluşturuluyor. Sohbet en fazla 12 tur sürecek.
group_chat = autogen.GroupChat(agents=[manager, developer, tester], messages=[], max_round=12)

# Grup sohbeti için bir yönetici atanıyor.
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=llm_config)

# Sohbeti başlatma ve yönetici ajanın yazılımcıya belirli bir görev vermesi
manager.initiate_chat(
    manager,
    # Yöneticinin yazılımcıdan, 0 ile 100 arasındaki asal sayıları yazdıran bir Python kodu yazmasını istemesi.
    message=""" Write a Python code that prints all prime numbers between 0 and 100 when executed."""
)
