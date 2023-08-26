import React, { useState } from 'react';
import CartItemList from './listaCarrinho';

const CartPage = () => {
  const [cartItems, setCartItems] = useState([
    {
      id: 1,
      name: 'Produto A',
      description: 'Descrição do Produto A',
      price: 19.99,
    },
    {
      id: 2,
      name: 'Produto B',
      description: 'Descrição do Produto B',
      price: 29.99,
    },
    {
      id: 3,
      name: 'Produto C',
      description: 'Descrição do Produto C',
      price: 9.99,
    },
  ]);

  const handleRemoveItem = (itemId) => {
    setCartItems(cartItems.filter(item => item.id !== itemId));
  };

  return (
    <div>
      <h1>Seu Carrinho</h1>
      <CartItemList cartItems={cartItems} onRemoveItem={handleRemoveItem} />
    </div>
  );
};

export default CartPage;
