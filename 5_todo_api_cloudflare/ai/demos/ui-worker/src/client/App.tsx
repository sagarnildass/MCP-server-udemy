import { useChat } from "@ai-sdk/react";
import { Center, Paper, Text, TextInput, Button, Group, ScrollArea, Stack } from "@mantine/core";

const ChatUI: React.FC = () => {
	const { messages, input, handleSubmit, handleInputChange } = useChat({
		keepLastMessageOnError: true,
		api: "/api",
	});

	return (
		<Center style={{ height: "100vh", backgroundColor: "#f5f5f5" }}>
			<Paper shadow="sm" p="md" style={{ width: "90%", maxWidth: 1000 }}>
				<ScrollArea style={{ height: 700, marginBottom: "1rem" }}>
					<Stack gap="xs">
						{messages.map((message) => (
							<Paper key={message.id} p="xs" shadow="xs">
								<Text>{message.role === "user" ? "User" : "Assistant"}:</Text>
								<Text>{message.content}</Text>
							</Paper>
						))}
					</Stack>
				</ScrollArea>
				<form onSubmit={handleSubmit}>
					<Group>
						<TextInput
							name="chat-input"
							value={input}
							onChange={handleInputChange}
							placeholder="Type your message..."
							style={{ flexGrow: 1 }}
						/>
						<Button type="submit" variant="filled">
							Send
						</Button>
					</Group>
				</form>
			</Paper>
		</Center>
	);
};

export default ChatUI;
