import React from "react";
import { Card, Typography, Row, Col } from "antd";

const { Title, Text } = Typography;

const cardStyle = {
  width: 340,
  margin: 16,
  boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)",
};

const titleStyle = {
  fontSize: 18,
};

const textStyle = {
  fontSize: 16,
  marginTop: 8,
};

const listaDeUsuarios = (props) => {
  const { listaUsuarios } = props;

  return (
    <Row gutter={16}>
      {listaUsuarios?.map((usuario, index) => (
        <Col span={5} key={index}>
          <Card title={"Informações do Usuário " + usuario.usuario} style={cardStyle}>
            <div>
              <Title level={4} style={titleStyle}>
                Nome
              </Title>
              <Text style={textStyle}>{usuario.nome}</Text>
              <Title level={4} style={titleStyle}>
                E-mail
              </Title>
              <Text style={textStyle}>{usuario.email}</Text>
              <Title level={4} style={titleStyle}>
                Telefone
              </Title>
              <Text style={textStyle}>{usuario.telefone}</Text>
              <Title level={4} style={titleStyle}>
                Endereço
              </Title>
              <Text style={textStyle}>{usuario.endereco}</Text>
            </div>
          </Card>
        </Col>
      ))}
    </Row>
  );
};

export default listaDeUsuarios;
