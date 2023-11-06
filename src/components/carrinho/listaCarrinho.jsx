import React from "react";
import { List, Card, Button, Typography } from "antd";

const { Text } = Typography;

const CartItemList = ({ cartItems, onRemoveItem }) => {
  const calcularQuantidadeProdutos = (carrinho) => {
    const quantidadeProdutos = {};

    carrinho.forEach((item) => {
      const { id, nome_produto } = item;
      const chave = `${id}-${nome_produto}`; // Usando uma chave única com id e nome_produto

      if (!quantidadeProdutos[chave]) {
        quantidadeProdutos[chave] = { ...item, quantidade: 1 };
      } else {
        quantidadeProdutos[chave].quantidade += 1;
      }
    });

    return Object.values(quantidadeProdutos);
  };

  const produtosUnicos = calcularQuantidadeProdutos(cartItems);

  return (
    <List
      dataSource={produtosUnicos}
      renderItem={(item) => (
        <List.Item>
          <Card title={item.nome_produto} style={{ width: "100%" }}>
            <Text>{item.descricao}</Text>
            <Text strong style={{ display: "block", marginTop: "8px" }}>
              Preço: R$ {item.preco}
            </Text>
            <Text style={{ display: "block", marginTop: "8px" }}>
              Quantidade: {item.quantidade}
            </Text>
            <Button
              type="primary"
              onClick={() => onRemoveItem(item.idproduto)}
              style={{ marginTop: "8px" }}
            >
              Remover
            </Button>
          </Card>
        </List.Item>
      )}
    />
  );
};

export default CartItemList;
