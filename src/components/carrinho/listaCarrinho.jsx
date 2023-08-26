import React from 'react';
import { List, Card, Button, Typography } from 'antd';

const { Text } = Typography;

const CartItemList = ({ cartItems, onRemoveItem }) => {
  return (
    <List
      dataSource={cartItems}
      renderItem={(item) => (
        <List.Item>
          <Card title={item.name} style={{ width: '100%' }}>
            <Text>{item.description}</Text>
            <Text strong style={{ display: 'block', marginTop: '8px' }}>
              Preço: R$ {item.price.toFixed(2)}
            </Text>
            <Button type="danger" onClick={() => onRemoveItem(item.id)} style={{ marginTop: '8px' }}>
              Remover
            </Button>
          </Card>
        </List.Item>
      )}
    />
  );
};

export default CartItemList;
