import React, { useState, useEffect } from 'react';
import CartItemList from './listaCarrinho';
import { Button } from 'antd';

const CartPage = () => {
  // Inicialize o estado do carrinho com base no localStorage ou uma lista vazia
  const [cartItems, setCartItems] = useState(() => {
    const savedCart = localStorage.getItem('cart');
    return savedCart ? JSON.parse(savedCart) : [];
  });

  // Atualize o localStorage sempre que o carrinho for alterado
  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(cartItems));
  }, [cartItems]);

  const handleRemoveItem = (itemId) => {
    // Remova o item do carrinho
    setCartItems((prevCart) => prevCart.filter(item => item.id !== itemId));
  };

  return (
    <div>
      <h1>Seu Carrinho</h1>
      <CartItemList cartItems={cartItems} onRemoveItem={handleRemoveItem} />
      <Button>Finalizar Compra</Button>
    </div>
  );
};

export default CartPage;
