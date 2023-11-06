import React, { useState, useEffect } from 'react';
import CartItemList from './listaCarrinho';
import { Button, Drawer, Modal, message, Form, Input, Select } from 'antd';

const { Option } = Select;

const CartPage = () => {
  //CARRINHO COMPLETO
  const [carrinho, setCarrinho] = useState(() => {
    const carrinhoSalvo = localStorage.getItem("carrinho");
    return carrinhoSalvo ? JSON.parse(carrinhoSalvo) : [];
  });

  const [clientes, setClientes] = useState(() => {
    const clientesSalvos = localStorage.getItem("clientes");
    return clientesSalvos ? JSON.parse(clientesSalvos) : [];
  });

  const [messageApi, contextHolder] = message.useMessage();

  const success = () => {
    messageApi.open({
      type: "success",
      content: "Um produto foi removido do carrinho",
    });
  };

  const successPedido = () => {
    messageApi.open({
      type: "success",
      content: "Pedido realizado com sucesso",
    });
  };

  // Atualize o localStorage sempre que o carrinho for alterado
  useEffect(() => {
    localStorage.setItem('carrinho', JSON.stringify(carrinho));
  }, [carrinho]);

  const handleRemoveItem = (itemId) => {
    // Encontre o índice do primeiro item com o ID correspondente
    const itemIndex = carrinho.findIndex((item) => item.idproduto === itemId);
  
    if (itemIndex !== -1) {
      // Se o índice foi encontrado, crie uma cópia do carrinho
      const novoCarrinho = [...carrinho];
  
      // Remova o item encontrado
      novoCarrinho.splice(itemIndex, 1);
  
      // Atualize o estado do carrinho
      setCarrinho(novoCarrinho);
      success();
    }
  };


  
  const [isModalOpen, setIsModalOpen] = useState(false);

  //FORM COM ID E TIPO DE PAGAMENTO
  const [formData, setFormData] = useState({
    IDCliente: "",
    tipoPagamento: "",
  });

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    //logica para realizar o pedido

    setCarrinho([]);
    setIsModalOpen(false);
    successPedido();
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  const somarPrecosDosProdutos = (produtos) => {
    let total = 0;
  
    for (const produto of produtos) {
      total += produto.preco;
    }
  
    return total;
  };
 

  return (
    <div>
      {contextHolder}
      <h1>Seu Carrinho</h1>
      <CartItemList cartItems={carrinho} onRemoveItem={handleRemoveItem} />
      <h2>Total: R$ {somarPrecosDosProdutos(carrinho)}</h2>
      <Button disabled={somarPrecosDosProdutos(carrinho) == 0} onClick={showModal}>Finalizar Compra</Button>
      <Modal
        title="Confirmação de Compra"
        visible={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <p>Confirme sua compra. Você está prestes a concluir a compra dos produtos no carrinho.</p>
        <p>Total: R$ {somarPrecosDosProdutos(carrinho)}</p>
        <Form>
          <Form.Item label="Cliente">
            <Select
              value={formData.IDCliente}
              onChange={(value) => setFormData({ ...formData, IDCliente: value })}
            >
              {clientes.map((cliente) => (
                <Option value={cliente.IDCliente}>{cliente.nome}</Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item label="Tipo de Pagamento">
            <Select
              value={formData.tipoPagamento}
              onChange={(value) => setFormData({ ...formData, tipoPagamento: value })}
            >
              <Option value="cartao">Cartão de Crédito</Option>
              <Option value="boleto">Boleto Bancário</Option>
            </Select>
          </Form.Item>
        </Form>
      </Modal>
    </div>
    
  );
};

export default CartPage;
