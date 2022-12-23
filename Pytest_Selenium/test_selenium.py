from time import sleep


def test_preencher_campos_pesquisas(browser):
    # Configuração
    dados = {
        'name': "Python",
        'email': "test@test.com",
        'senha': "12345",
        
    }
    
    browser.get("http://selenium.dunosauro.live/aula_07")
    sleep(2)
    form = browser.find_element_by_tag_name('form')
    
    #Ações
    form.find_element_by_name("nome").send_keys(dados['name'])
    form.find_element_by_name("email").send_keys(dados['email'])
    form.find_element_by_name("senha").send_keys(dados['senha'])
    form.find_element_by_id("btn").click()
    
    import ipdb; ipdb.set_trace()
        
    # Assertiva
    assert 0
        
    


