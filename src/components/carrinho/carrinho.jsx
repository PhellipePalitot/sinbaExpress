import React, { useState, useEffect } from 'react';
import CartItemList from './listaCarrinho';
import { Button, Drawer, Modal } from 'antd';

const CartPage = () => {
  const [carrinho, setCarrinho] = useState(() => {
    const carrinhoSalvo = localStorage.getItem("carrinho");
    return carrinhoSalvo ? JSON.parse(carrinhoSalvo) : [];
  });

  // Atualize o localStorage sempre que o carrinho for alterado
  useEffect(() => {
    localStorage.setItem('carrinho', JSON.stringify(carrinho));
  }, [carrinho]);

  const handleRemoveItem = (itemId) => {
    // Encontre o índice do primeiro item com o ID correspondente
    const itemIndex = carrinho.findIndex((item) => item.id === itemId);
  
    if (itemIndex !== -1) {
      // Se o índice foi encontrado, crie uma cópia do carrinho
      const novoCarrinho = [...carrinho];
  
      // Remova o item encontrado
      novoCarrinho.splice(itemIndex, 1);
  
      // Atualize o estado do carrinho
      setCarrinho(novoCarrinho);
    }
  };
  
  const [isModalOpen, setIsModalOpen] = useState(false);

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    setIsModalOpen(false);
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
      <h1>Seu Carrinho</h1>
      <CartItemList cartItems={carrinho} onRemoveItem={handleRemoveItem} />
      <h2>Total: R$ {somarPrecosDosProdutos(carrinho)}</h2>
      <Button onClick={showModal}>Finalizar Compra</Button>
      <Modal title="Basic Modal" open={isModalOpen} onOk={handleOk} onCancel={handleCancel}>
        <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p>
      </Modal>
    </div>
    
  );
};

export default CartPage;
