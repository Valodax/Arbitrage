import { Token } from "../Main"
import { useEthers, useTokenBalance } from "@usedapp/core"

export interface WalletBalanceProps {
    token: Token
}

export const WalletBalance = ({ token }: WalletBalanceProps) => {
    const { image, address, name } = token
    const { account } = useEthers()
    const tokenBalance = useTokenBalance(address, account)
    console.log(tokenBalance?.toString())
    return (<div>I'm the wallet balance</div>)
}