package com.raventune.jewishcraft.init;

import java.util.function.Function;

import com.google.common.base.Supplier;
import com.raventune.jewishcraft.Jewishcraft;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.Item.Properties;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;
import net.minecraft.world.level.material.MaterialColor;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class BlockInit {
	
	public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, Jewishcraft.MOD_ID);
	
	public static final RegistryObject<Block> SILVER_ORE = register("silver_ore", () -> new Block(BlockBehaviour.Properties.of(Material.METAL, MaterialColor.STONE)),
			object -> () -> new Item(new Item.Properties().tab(Jewishcraft.JEWISHCRAFT_TAB)));
	
	public static final DeferredRegister<Item> ITEMS =ItemInit.ITEMS;
	
	private static <T extends Block> RegistryObject<T> registerBlock(final String name, final Supplier<? extends T> block) {
		return BLOCKS.register(name, block);
}

	private static <T extends Block> RegistryObject<T> register(final String name, final Supplier<? extends T> block, Function<RegistryObject<T>,Supplier<? extends Item>> item) {
		RegistryObject<T> obj = registerBlock(name, block);
		ITEMS.register(name,item.apply(obj) );
		return obj;
}
	
}