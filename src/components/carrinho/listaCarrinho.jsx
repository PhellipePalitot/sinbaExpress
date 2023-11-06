import React from 'react';
import { List, Card, Button, Typography } from 'antd';

const { Text } = Typography;

const CartItemList = ({ cartItems, onRemoveItem }) => {
  return (
    <List
      dataSource={cartItems}
      renderItem={(item) => (
        <List.Item>
          <Card title={item.nome_produto} style={{ width: '100%' }}>
            <Text>{item.descricao}</Text>
            <Text strong style={{ display: 'block', marginTop: '8px' }}>
              Preço: R$ {item.preco}
            </Text>
            <Button type="primary" onClick={() => onRemoveItem(item.id)} style={{ marginTop: '8px' }}>
              Remover
            </Button>
          </Card>
        </List.Item>
      )}
    />
  );
};

export default CartItemList;
