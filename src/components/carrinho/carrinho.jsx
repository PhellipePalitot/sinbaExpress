import React, { useState, useEffect } from 'react';
import CartItemList from './listaCarrinho';
import { Button } from 'antd';

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
    // Remova o item do carrinho
    setCarrinho((prevCart) => prevCart.filter(item => item.id !== itemId));
  };

  return (
    <div>
      <h1>Seu Carrinho</h1>
      <CartItemList cartItems={carrinho} onRemoveItem={handleRemoveItem} />
      <Button>Finalizar Compra</Button>
    </div>
  );
};

export default CartPage;
