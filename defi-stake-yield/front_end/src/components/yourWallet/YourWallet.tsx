import { Token } from "../Main"
import React, { useState } from "react"
import { Box } from "@material-ui/core"
import { TabContext, TabList, TabPanel } from "@material-ui/lab"

interface YourWalletProps {
    supportedTokens: Array<Token>
}
export const YourWallet = ({ supportedTokens }: YourWalletProps) => {
    const [selectedTokenIndex, setSelectedTokenIndex] = useState<number>(0)
    return (
        <Box>
            <h1>Your Wallet!</h1>
            <Box>
                <TabContext value={selectedTokenIndex.toString()}>
                </TabContext>
            </Box>
        </Box>
    )
}