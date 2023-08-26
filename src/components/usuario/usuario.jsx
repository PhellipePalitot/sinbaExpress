import React from 'react';
import { Card, Typography } from 'antd';

const { Title, Text } = Typography;

const UserProfile = () => {
  return (
    <Card title="Informações do Usuário">
      <div style={{ padding: '24px' }}>
        <Title level={4}>Nome</Title>
        <Text>John Doe</Text>
        <Title level={4} style={{ marginTop: '16px' }}>E-mail</Title>
        <Text>john.doe@example.com</Text>
        <Title level={4} style={{ marginTop: '16px' }}>Telefone</Title>
        <Text>(123) 456-7890</Text>
        <Title level={4} style={{ marginTop: '16px' }}>Endereço</Title>
        <Text>
          123 Main Street,
          <br />
          City, State, Zip Code
        </Text>
      </div>
    </Card>
  );
};

export default UserProfile;
