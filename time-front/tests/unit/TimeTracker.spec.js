import Vuex from 'vuex';
import { mount, createLocalVue } from '@vue/test-utils';
import state from './store-config'
import TimeInput from '@/components/TimeInput.vue';
import TimeEntry from '@/components/TimeEntry.vue';

const localVue = createLocalVue();
localVue.use(Vuex);

describe('TimeEntry TimeInput tests', () => {

  it('TimeImput displays correct value', () => {
    const timestamp = 1647107814;
    const wrapper = mount(TimeInput, {
      propsData: { timestamp }
    });
    wrapper.vm.$nextTick(() => {
      const input = wrapper.vm.$refs.inputRef.$refs.input.value;
      expect(input).toBe('18:56');
    });
  });

  it('TimeInput emits changed timestamp', async () => {
    const timestamp = 1647107814;
    const wrapper = mount(TimeInput, {
      propsData: { timestamp }
    });
    await wrapper.vm.$nextTick();
    await wrapper.vm.inputFocus();
    let input = wrapper.get('input');
    input.setValue('1232');
    await wrapper.vm.inputBlur();
    expect(wrapper.emitted('timeChanged')[0][0]).toBe(1647084774);
  });

  it('TimeInput not emits changed timestamp after incorrect time is set', async () => {
    const timestamp = 1647107814; // 18:56
    const wrapper = mount(TimeInput, {
      propsData: { timestamp }
    });
    await wrapper.vm.$nextTick();
    await wrapper.vm.inputFocus();
    let input = wrapper.get('input');
    input.setValue('3423');
    await wrapper.vm.inputBlur();
    expect(input.element.value).toBe('18:56');
    expect(wrapper.emitted('timeChanged')).toBeFalsy();
  });
});
describe('TimeEntry Tests', () => {

  it('TimeEntry displays description', async () => {
    const wrapper = mount(TimeEntry, {
      propsData: { timeEntryID: 1 },
      mocks: {
        $store: {
          state: state
        }
      },
      localVue
    });
    await wrapper.vm.$nextTick();
    let descInput = wrapper.get('.desc-input').get('input');
    expect(descInput.element.value).toBe('Some desc')
  });

  it('TimeEntry can change description and emits "dataChanged"', async () => {
    const wrapper = mount(TimeEntry, {
      propsData: { timeEntryID: 1 },
      mocks: {
        $store: {
          state: state
        }
      },
      localVue
    });
    await wrapper.vm.$nextTick();

    wrapper.vm.copyValue(wrapper.vm.description)
    let descInput = wrapper.get('.desc-input').get('input');
    await descInput.setValue('Changed description')
    await wrapper.vm.setDescription()

    expect(descInput.element.value).toBe('Changed description')
  });
});
